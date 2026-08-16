---
type: Handbook
title: 職務経歴書データ仕様
description: data/*.yml の構造と記述規約。README と公開サイトはこのデータから生成される。
resource: https://github.com/kazuya0araki/resume
tags: [resume, schema, yaml]
timestamp: 2026-08-16T00:00:00Z
---

職務経歴書の内容は `data/` 配下の YAML が唯一のソースで、
`README.md` / `README_EN.md` と公開サイトはそこから生成される。

このバンドルはその YAML の仕様を Open Knowledge Format で記述したもの。
スキーマ表は実データから導出しているため、仕様と実物がずれない。

# 構成

| | 内容 |
|---|---|
| [ファイル](files/index.md) | `data/*.yml` 各ファイルのスキーマ |
| [記述規約](conventions/index.md) | 対訳・日付・URL・リストの持ち方 |
| [変更履歴](log.md) | 仕様の変更記録 |

# 編集の手順

1. `data/` 配下の該当ファイルを編集する
2. 生成コマンドを実行し、`README.md` / `README_EN.md` / 公開サイトを更新する
3. 生成物とあわせてコミットする

`data/` を直接編集し、`README.md` は編集しない。
