---
type: Convention
title: 日付の持ち方
description: 日付を ISO で 1 度だけ保持する規約。
tags: [dates, iso8601]
timestamp: 2026-08-16T00:00:00Z
---

| 用途 | 形式 | 例 |
|---|---|---|
| 在籍期間 | `YYYY-MM` | `2026-07` |
| 実績の日付 | `YYYY-MM-DD` | `2024-11-23` |
| 継続中 | `to` を `null` | |

日本語の「2026年07月」、英語の `July 2026` はいずれも生成時に組み立てる。
`to` が `null` のとき、生成側は `meta.labels.*.now`（現在 / Currently）を出す。

`career[].rows` の期間から在籍期間を導出できるため、
概要表と詳細表で期間が食い違うことがない。

# 関連

- [記述規約](index.md)
- [ファイル一覧](../files/index.md)
