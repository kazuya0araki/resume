---
type: Schema
title: data/skills.yml
description: 念能力6系統・ポートフォリオと、OS / 言語 / ミドルウェア / クラウド / IDE / ツールの各区分。
resource: https://github.com/kazuya0araki/resume/blob/main/data/skills.yml
tags: [schema, skills]
timestamp: 2026-08-16T00:00:00Z
---

念能力6系統・ポートフォリオと、OS / 言語 / ミドルウェア / クラウド / IDE / ツールの各区分。

対応する章は「スキル」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `title` | 文字列（対訳） | ○ |  | スキル |
| `nen.title` | 文字列（対訳） | ○ |  | HUNTER×HUNTERの念能力6系統で喩えるデータ分析スキル |
| `nen.url` | URL | ○ |  | https://tjo.hatenablog.com/entry/2018/… |
| `nen.systems[].name` | 文字列（対訳） | ○ |  | 強化系 |
| `nen.systems[].aspect` | 文字列（対訳） | ○ |  | モデリング |
| `nen.systems[].level` | 整数 | ○ | 6 系統それぞれの自己評価値。 | 1 |
| `nen.image` | 文字列 | ○ |  | ./image/nen.png |
| `nen.viz_url` | URL | ○ |  | https://public.tableau.com/app/profile… |
| `portfolio.title` | 文字列（対訳） | ○ |  | ポートフォリオ |
| `portfolio.items[].name` | 文字列 | ○ |  | Tableau Public |
| `portfolio.items[].url` | URL | ○ |  | https://public.tableau.com/app/profile… |
| `sections[].key` | 文字列 | ○ | 区分の識別子。生成側が参照する。 | os |
| `sections[].title` | 文字列 | ○ |  | OS |
| `sections[].groups[].name` | 文字列 | ○ |  | Microsoft Windows |
| `sections[].groups[].items[].name` | 文字列 | ○ |  | Windows 95 and later |
| `sections[].items[].name` | 文字列 | ○ |  | Java |
| `sections[].items[].note` | 文字列 |  |  | Terraform |
| `sections[].related.title` | 文字列（対訳） |  |  | 関連パッケージ、ツール |
| `sections[].related.groups[].language` | 文字列 | ○ |  | Java |
| `sections[].related.groups[].items[].name` | 文字列 | ○ |  | Spring Framework |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
