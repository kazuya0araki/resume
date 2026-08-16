---
type: Schema
title: data/career.yml
description: 在籍企業と、企業ごとの所属組織・職位・業務内容。
resource: https://github.com/kazuya0araki/resume/blob/main/data/career.yml
tags: [schema, career]
timestamp: 2026-08-16T00:00:00Z
---

在籍企業と、企業ごとの所属組織・職位・業務内容。

対応する章は「職務経歴」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `career[].company` | 文字列（対訳） | ○ | 社名。 | アロウズ・システム株式会社 |
| `career[].url` | URL |  | 企業サイト。 | https://lanstech.co.jp/2025/06/02/%e5%… |
| `career[].note` | 文字列（対訳） |  | 社名に括弧書きで添える補足。 | 株式会社ランステックに吸収合併 |
| `career[].rows[].from` | 年月（YYYY-MM） | ○ | 開始年月（YYYY-MM）。 | 2007-05 |
| `career[].rows[].to` | 年月（YYYY-MM） | ○ | 終了年月。省略・null は「現在」。 | 2011-04 |
| `career[].rows[].org` | 文字列（対訳） | ○ | 所属組織。 | オープンシステム開発部 |
| `career[].rows[].role` | 文字列（対訳） | ○ | 職位。 | システムエンジニア メンバー |
| `career[].rows[].items[]` | 文字列（対訳） | ○ |  | SAP製品アドイン開発(Java, ABAP) |
| `career[].suffix` | 文字列（対訳） |  | 日英で書式が異なる補足を、書いたとおりに社名の後ろへ連結する。 | (現、[株式会社ラキール](https://www.lakeel.com/j… |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
