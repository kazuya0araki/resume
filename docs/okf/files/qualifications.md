---
type: Schema
title: data/qualifications.yml
description: 保有資格の一覧。
resource: https://github.com/kazuya0araki/resume/blob/main/data/qualifications.yml
tags: [schema, qualifications]
timestamp: 2026-08-16T00:00:00Z
---

保有資格の一覧。

対応する章は「資格」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `title` | 文字列（対訳） | ○ |  | 資格 |
| `qualifications[].name` | 文字列（対訳） | ○ |  | 実用数学技能検定3級 |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
