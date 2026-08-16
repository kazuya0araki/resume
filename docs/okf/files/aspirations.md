---
type: Schema
title: data/aspirations.yml
description: 今後取り組みたいこと。
resource: https://github.com/kazuya0araki/resume/blob/main/data/aspirations.yml
tags: [schema, aspirations]
timestamp: 2026-08-16T00:00:00Z
---

今後取り組みたいこと。

対応する章は「どんなことがしたいか」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `title` | 文字列（対訳） | ○ |  | どんなことがしたいか？ |
| `items[].title` | 文字列（対訳） | ○ |  | 社会貢献度の高いデータを安心安全に利活用したい |
| `items[].lead` | 文字列（対訳） |  | 箇条書きの前置き。 | 日常座臥、以下を考えています; |
| `items[].questions[]` | 文字列（対訳） |  |  | 安心安全なデータプラットフォームが提供できないか？ |
| `items[].statements[]` | 文字列（対訳） |  |  | データリテラシーの高い人材が今後のビジネスを劇的に変革する力があると私は考え… |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
