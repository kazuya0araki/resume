---
type: Schema
title: data/mission.yml
description: 行動指針と座右の銘。
resource: https://github.com/kazuya0araki/resume/blob/main/data/mission.yml
tags: [schema, mission]
timestamp: 2026-08-16T00:00:00Z
---

行動指針と座右の銘。

対応する章は「Mission / Vision / Value」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `title` | 文字列 | ○ |  | Mission / Vision / Value |
| `mission.title` | 文字列 | ○ |  | Mission |
| `mission.statement` | 文字列（対訳） | ○ |  | データの力で世界を変革するトリックスターとして、人々を導く存在となる |
| `vision.title` | 文字列 | ○ |  | Vision |
| `vision.statement` | 文字列（対訳） | ○ |  | データの導き手として、価値あることを正しく行う |
| `value.title` | 文字列 | ○ |  | Value |
| `value.statement` | 文字列（対訳） | ○ |  | QCDSを当たり前に体現する |
| `value.items[].key` | 文字列 | ○ |  | Quality |
| `value.items[].label` | 文字列 | ○ |  | High Outcome |
| `value.items[].body` | 文字列（対訳） | ○ |  | 当たり前に高品質、高成果物を目指す。 |
| `motto.title` | 文字列（対訳） | ○ |  | 座右の銘 |
| `motto.items[]` | 文字列 | ○ |  | The right thing in the right way. |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
