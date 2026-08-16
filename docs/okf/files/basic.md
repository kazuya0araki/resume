---
type: Schema
title: data/basic.yml
description: 氏名・生年月日・性別・居住地と SNS アカウント。
resource: https://github.com/kazuya0araki/resume/blob/main/data/basic.yml
tags: [schema, basic]
timestamp: 2026-08-16T00:00:00Z
---

氏名・生年月日・性別・居住地と SNS アカウント。

対応する章は「基本情報」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `name` | 文字列（対訳） | ○ |  | 荒木 和也 |
| `birth` | 日付（YYYY-MM-DD） | ○ | 生年月日。ISO で保持し、表記は言語ごとに組み立てる。 | 1982-08-30 |
| `sex` | 文字列（対訳） | ○ |  | 男 |
| `residence` | 文字列（対訳） | ○ |  | 東京都 |
| `social[].service` | 文字列 | ○ | バッジに表示するサービス名。 | X(twitter) |
| `social[].logo` | 文字列 | ○ | shields.io のロゴ識別子。 | x |
| `social[].color` | 整数 | ○ | バッジの背景色（6 桁の 16 進数）。 | 0 |
| `social[].handle` | 文字列 | ○ | そのサービスでのアカウント名。 | kazuya_araki_jp |
| `social[].url` | URL | ○ |  | https://twitter.com/kazuya_araki_jp |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
