---
type: Schema
title: data/interests.yml
description: データ × 他分野の関心領域と読書。
resource: https://github.com/kazuya0araki/resume/blob/main/data/interests.yml
tags: [schema, interests]
timestamp: 2026-08-16T00:00:00Z
---

データ × 他分野の関心領域と読書。

対応する章は「興味があるもの」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `title` | 文字列（対訳） | ○ |  | 興味があるもの |
| `cross.title` | 文字列（対訳） | ○ |  | データ × ○○ |
| `cross.topics[].title` | 文字列（対訳） | ○ |  | データ × デザイン = ビジュアルアナリティクス |
| `cross.topics[].images[]` | 文字列 |  |  | ./image/Art_and_Science_of_Visual_Anal… |
| `cross.topics[].lead[]` | 文字列（対訳） |  |  | データサイエンスは、マーケティングと親和性の高い分野です。 |
| `cross.topics[].groups[].name` | 文字列（対訳） | ○ |  | データ分析基盤、CRM環境の設計、構築、運用 |
| `cross.topics[].groups[].items[].name` | 文字列 | ○ |  | Data Warehouse |
| `cross.topics[].groups[].items[].items[].name` | 文字列 | ○ |  | Google BigQuery |
| `reading.title` | 文字列（対訳） | ○ |  | 読書 |
| `reading.themes.title` | 文字列（対訳） | ○ |  | テーマ |
| `reading.themes.items[].name` | 文字列（対訳） | ○ |  | ビジネス |
| `reading.notes[]` | 文字列（対訳） | ○ |  | テーマについて議論し、書評を述べるアウトプットや発散が重要だと考えています。 |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
