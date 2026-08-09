#!/usr/bin/env python3
"""data/resume.yml を単一のソースとして README / HTML を生成する。

    python3 scripts/build.py                # README.md, README_EN.md, docs/ を更新
    python3 scripts/build.py --out build    # 出力先を変える（差分レビュー用）
    python3 scripts/build.py --check        # 生成物が最新か確認するだけ（CI 用）
    python3 scripts/build.py --strict       # 警告が 1 件でもあれば異常終了

設計:
    YAML → 中間ドキュメントモデル（見出し・段落・表・リスト）→ Markdown / HTML
    という 2 段構成。章の構成は build_document() の 1 箇所だけが持ち、
    Markdown と HTML の描画はそこから機械的に落とすので、両者がずれない。
"""
from __future__ import annotations

import argparse
import datetime
import html
import re
import sys
import unicodedata
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "resume.yml"
TEMPLATES = ROOT / "templates"
ASSETS = ROOT / "assets"

MONTHS_EN = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
LINK_RE = re.compile(r"\[([^\]]+)\]\[([A-Za-z0-9_.-]+)\]")
EMPHASIS_RE = re.compile(r"\*([^*]+)\*")


# --------------------------------------------------------------------------
# コンテキスト
# --------------------------------------------------------------------------
class Ctx:
    """1 言語ぶんの描画コンテキスト。翻訳漏れ等の警告もここに溜める。"""

    def __init__(self, data: dict, lang: str):
        self.lang = lang
        self.links: dict = data.get("links") or {}
        self.labels: dict = (data.get("labels") or {}).get(lang, {})
        self.warnings: list[str] = []

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def label(self, key: str) -> str:
        if key not in self.labels:
            self.warn(f"[{self.lang}] labels.{key} が未定義です")
            return key
        return self.labels[key]

    def text(self, value, where: str = "") -> str:
        """スカラー = 全言語共通、マップ = 言語別。未訳は警告して日本語にフォールバック。"""
        if value is None:
            return ""
        if isinstance(value, dict):
            if self.lang in value:
                return str(value[self.lang])
            fallback = value.get("ja", next(iter(value.values()), ""))
            self.warn(f"[{self.lang}] 未翻訳: {where or fallback}")
            return str(fallback)
        return str(value)


# --------------------------------------------------------------------------
# 日付
# --------------------------------------------------------------------------
def _ordinal(n: int) -> str:
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return f"{n}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th') }"


def fmt_month(value: str | None, ctx: Ctx) -> str:
    """'2026-03' → '2026年03月' / 'March 2026'。None は「現在 / Currently」。"""
    if value in (None, ""):
        return ctx.label("now")
    year, month = str(value).split("-")[:2]
    if ctx.lang == "ja":
        return f"{year}年{int(month):02d}月"
    return f"{MONTHS_EN[int(month) - 1]} {year}"


def fmt_date(value, ctx: Ctx) -> str:
    """date → '2026年07月01日' / 'July 1st, 2026'。"""
    if isinstance(value, str):
        value = datetime.date.fromisoformat(value)
    if ctx.lang == "ja":
        return f"{value.year}年{value.month:02d}月{value.day:02d}日"
    return f"{MONTHS_EN[value.month - 1]} {_ordinal(value.day)}, {value.year}"


def fmt_range(start, end, ctx: Ctx) -> str:
    return ctx.label("range") % (fmt_month(start, ctx), fmt_month(end, ctx))


# --------------------------------------------------------------------------
# ドキュメントモデル
# --------------------------------------------------------------------------
def H(level: int, text: str) -> dict:
    return {"t": "h", "level": level, "text": text}


def P(text: str) -> dict:
    return {"t": "p", "text": text}


def Table(head: list[str], rows: list[list]) -> dict:
    return {"t": "table", "head": head, "rows": rows}


def UL(items: list) -> dict:
    return {"t": "ul", "items": items}


def Badges(items: list[dict]) -> dict:
    return {"t": "badges", "items": items}


def career_span(entry: dict, ctx: Ctx) -> tuple[str | None, str | None]:
    """概要表の期間。rows があればそこから導出し、明示値とずれていれば警告する。"""
    rows = entry.get("rows") or []
    if rows:
        start = min(str(r["from"]) for r in rows)
        end = None if any(r.get("to") in (None, "") for r in rows) else max(str(r["to"]) for r in rows)
        for key, derived in (("from", start), ("to", end)):
            declared = entry.get(key)
            declared = None if declared in (None, "") else str(declared)
            if key in entry and declared != derived:
                ctx.warn(
                    f"career.{entry['key']}.{key} が明示値 {declared!r} と "
                    f"詳細から導出した {derived!r} で食い違っています"
                )
        return start, end
    return (
        None if entry.get("from") in (None, "") else str(entry["from"]),
        None if entry.get("to") in (None, "") else str(entry["to"]),
    )


def company_cell(entry: dict, ctx: Ctx) -> str:
    """社名セル。

    note   … 括弧で囲って社名に添える（link がある場合はリンクの内側に入る）
    suffix … 言語ごとに書式が違う場合の逃げ道。書いたとおりに後ろへ連結する
    """
    name = ctx.text(entry["company"], f"career.{entry['key']}.company")

    if entry.get("note"):
        note = ctx.text(entry["note"], f"career.{entry['key']}.note")
        name = f"{name}({note})"
    if entry.get("link"):
        name = f"[{name}][{entry['link']}]"
    if entry.get("suffix"):
        name += ctx.text(entry["suffix"], f"career.{entry['key']}.suffix")
    return name


def build_document(data: dict, ctx: Ctx) -> list[dict]:
    """章の構成を定義する唯一の場所。"""
    blocks: list[dict] = []
    L = ctx.label

    # ---- 見出しと更新日 -------------------------------------------------
    blocks.append(H(1, L("doc_title")))
    blocks.append(P(L("as_of") % fmt_date(data["meta"]["updated"], ctx)))
    blocks.append({"t": "langlink", "text": L("other_lang")})

    # ---- 基本情報 -------------------------------------------------------
    basic = data["basic"]
    blocks.append(H(2, L("basic")))
    blocks.append(H(3, L("name")))
    blocks.append(P(ctx.text(basic["name"], "basic.name")))
    blocks.append(H(3, L("birth")))
    blocks.append(P(fmt_date(basic["birth"], ctx)))
    blocks.append(H(3, L("sex")))
    blocks.append(P(ctx.text(basic["sex"], "basic.sex")))
    blocks.append(H(3, L("residence")))
    blocks.append(P(ctx.text(basic["residence"], "basic.residence")))
    blocks.append(H(3, L("sns")))
    blocks.append(Badges(basic["social"]))

    # ---- 職務経歴 -------------------------------------------------------
    blocks.append(H(2, L("career")))
    blocks.append(H(3, L("overview")))
    overview_rows = []
    for entry in data["career"]:
        start, end = career_span(entry, ctx)
        overview_rows.append([fmt_range(start, end, ctx), company_cell(entry, ctx)])
    blocks.append(Table([L("th_term"), L("th_company")], overview_rows))

    detailed = [e for e in data["career"] if e.get("rows")]
    if detailed:
        blocks.append(H(3, L("detail")))
        for entry in detailed:
            blocks.append(H(4, ctx.text(entry["company"], f"career.{entry['key']}.company")))
            rows = []
            for i, row in enumerate(entry["rows"]):
                where = f"career.{entry['key']}.rows[{i}]"
                rows.append([
                    fmt_range(row.get("from"), row.get("to"), ctx),
                    ctx.text(row["org"], f"{where}.org"),
                    ctx.text(row["role"], f"{where}.role"),
                    [ctx.text(it, f"{where}.items") for it in row["items"]],
                ])
            blocks.append(Table(
                [L("th_period"), L("th_org"), L("th_role"), L("th_content")], rows,
            ))

    # ---- 資格 -----------------------------------------------------------
    blocks.append(H(2, L("qualifications")))
    blocks.append(UL([ctx.text(q, "qualifications") for q in data["qualifications"]]))

    return blocks


# --------------------------------------------------------------------------
# 描画: Markdown
# --------------------------------------------------------------------------
def md_text(text: str, ctx: Ctx) -> str:
    def repl(m: re.Match) -> str:
        label, key = m.group(1), m.group(2)
        if key not in ctx.links:
            ctx.warn(f"links.{key} が未登録です（参照: {label}）")
            return label
        return f"[{label}]({ctx.links[key]})"

    return LINK_RE.sub(repl, text)


def md_cell(cell, ctx: Ctx) -> str:
    if isinstance(cell, list):
        if len(cell) == 1:
            return md_text(cell[0], ctx)
        return "<br>".join(f"- {md_text(c, ctx)}" for c in cell)
    return md_text(cell, ctx)


def render_markdown(blocks: list[dict], ctx: Ctx, other_lang_path: str) -> str:
    out: list[str] = []
    for b in blocks:
        kind = b["t"]
        if kind == "h":
            out.append(f"{'#' * b['level']} {md_text(b['text'], ctx)}")
        elif kind == "p":
            out.append(md_text(b["text"], ctx))
        elif kind == "langlink":
            out.append(f"[{b['text']}]({other_lang_path})")
        elif kind == "table":
            out.append("|" + "|".join(md_text(h, ctx) for h in b["head"]) + "|")
            out.append("|" + "|".join("---" for _ in b["head"]) + "|")
            for row in b["rows"]:
                out.append("|" + "|".join(md_cell(c, ctx) for c in row) + "|")
        elif kind == "ul":
            for item in b["items"]:
                out.append(f"- {md_text(item, ctx)}")
        elif kind == "badges":
            for s in b["items"]:
                service = s["service"].replace(" ", "%20")
                badge = (
                    f"https://img.shields.io/badge/{service}-{s['color']}"
                    f"?style=for-the-badge&logo={s['logo']}&logoColor=white"
                )
                out.append(f"[![{s['handle']}]({badge})]({s['url']})")
        out.append("")

    # 見出しの直前を必ず 1 行あける（Markdown の体裁を安定させる）
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


# --------------------------------------------------------------------------
# 描画: HTML
# --------------------------------------------------------------------------
def _plain_to_html(text: str) -> str:
    """エスケープしたうえで、*強調* だけ Markdown と同じ意味に落とす。"""
    return EMPHASIS_RE.sub(r"<em>\1</em>", html.escape(text))


def html_text(text: str, ctx: Ctx) -> str:
    """[label][key] をアンカーにし、それ以外はエスケープする。"""
    parts: list[str] = []
    pos = 0
    for m in LINK_RE.finditer(text):
        parts.append(_plain_to_html(text[pos:m.start()]))
        label, key = m.group(1), m.group(2)
        if key in ctx.links:
            url = html.escape(ctx.links[key], quote=True)
            parts.append(f'<a href="{url}">{_plain_to_html(label)}</a>')
        else:
            ctx.warn(f"links.{key} が未登録です（参照: {label}）")
            parts.append(_plain_to_html(label))
        pos = m.end()
    parts.append(_plain_to_html(text[pos:]))
    return "".join(parts)


def html_cell(cell, ctx: Ctx) -> str:
    if isinstance(cell, list):
        if len(cell) == 1:
            return html_text(cell[0], ctx)
        items = "".join(f"<li>{html_text(c, ctx)}</li>" for c in cell)
        return f"<ul>{items}</ul>"
    return html_text(cell, ctx)


def render_html_body(blocks: list[dict], ctx: Ctx, other_lang_href: str) -> str:
    out: list[str] = []
    for b in blocks:
        kind = b["t"]
        if kind == "h":
            level = b["level"]
            out.append(f"<h{level}>{html_text(b['text'], ctx)}</h{level}>")
        elif kind == "p":
            out.append(f"<p>{html_text(b['text'], ctx)}</p>")
        elif kind == "langlink":
            out.append(
                f'<p class="langlink"><a href="{other_lang_href}">'
                f"{html_text(b['text'], ctx)}</a></p>"
            )
        elif kind == "table":
            head = "".join(f"<th>{html_text(h, ctx)}</th>" for h in b["head"])
            rows = "".join(
                "<tr>" + "".join(f"<td>{html_cell(c, ctx)}</td>" for c in row) + "</tr>"
                for row in b["rows"]
            )
            out.append(
                '<div class="table-scroll"><table>'
                f"<thead><tr>{head}</tr></thead><tbody>{rows}</tbody>"
                "</table></div>"
            )
        elif kind == "ul":
            items = "".join(f"<li>{html_text(i, ctx)}</li>" for i in b["items"])
            out.append(f"<ul>{items}</ul>")
        elif kind == "badges":
            chips = "".join(
                f'<a class="chip" href="{html.escape(s["url"], quote=True)}">'
                f'{html.escape(s["service"])}</a>'
                for s in b["items"]
            )
            out.append(f'<div class="chips">{chips}</div>')
    return "\n".join(out)


# --------------------------------------------------------------------------
# 生成
# --------------------------------------------------------------------------
OUTPUTS = {
    "ja": {"md": "README.md", "html": "docs/index.html", "other_md": "./README_EN.md", "other_html": "./en/"},
    "en": {"md": "README_EN.md", "html": "docs/en/index.html", "other_md": "./README.md", "other_html": "../"},
}


def generate(data: dict) -> tuple[dict[str, str], list[str]]:
    """出力パス → 中身 の辞書と、全言語ぶんの警告を返す。"""
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=False)
    template = env.get_template("page.html")
    files: dict[str, str] = {}
    warnings: list[str] = []

    for lang in data["meta"]["languages"]:
        ctx = Ctx(data, lang)
        blocks = build_document(data, ctx)
        spec = OUTPUTS[lang]

        files[spec["md"]] = render_markdown(blocks, ctx, spec["other_md"])
        files[spec["html"]] = template.render(
            lang=lang,
            title=ctx.label("doc_title"),
            name=ctx.text(data["basic"]["name"], "basic.name"),
            updated=fmt_date(data["meta"]["updated"], ctx),
            css_href="assets/style.css" if lang == "ja" else "../assets/style.css",
            body=render_html_body(blocks, ctx, spec["other_html"]),
        )
        warnings += ctx.warnings

    files["docs/.nojekyll"] = ""
    files["docs/assets/style.css"] = (ASSETS / "style.css").read_text(encoding="utf-8")

    # 「アロウズ」の濁点が結合文字になっている等の表記ゆれを防ぐため NFC に揃える。
    # （現行 README.md には NFD の箇所が 5 件あり、grep や検索で一致しない状態）
    files = {k: unicodedata.normalize("NFC", v) for k, v in files.items()}

    # 同じ指摘が Markdown / HTML の両描画で出るので、順序を保って一意化する。
    return files, list(dict.fromkeys(warnings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=".", help="出力先ディレクトリ（既定: リポジトリ直下）")
    parser.add_argument("--check", action="store_true", help="書き込まず、生成物が最新かだけ確認する")
    parser.add_argument("--strict", action="store_true", help="警告があれば異常終了する")
    args = parser.parse_args()

    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    files, warnings = generate(data)

    out_root = (ROOT / args.out).resolve()
    stale: list[str] = []

    for rel, content in sorted(files.items()):
        path = out_root / rel
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == content:
            continue
        stale.append(rel)
        if not args.check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    for w in warnings:
        print(f"warning: {w}", file=sys.stderr)

    if args.check:
        if stale:
            print("生成物が resume.yml と一致していません:", file=sys.stderr)
            for rel in stale:
                print(f"  - {rel}", file=sys.stderr)
            print("`python3 scripts/build.py` を実行してコミットしてください。", file=sys.stderr)
            return 1
        print("生成物は最新です。")
    else:
        for rel in stale:
            print(f"updated: {rel}")
        if not stale:
            print("変更はありません。")

    if warnings and args.strict:
        print(f"警告 {len(warnings)} 件のため異常終了しました（--strict）。", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
