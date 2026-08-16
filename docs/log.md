---
type: Log
title: 変更履歴
description: データ仕様の変更記録。
tags: [log]
timestamp: 2026-08-16T00:00:00Z
---

# 2026-08-16

`README.md` / `README_EN.md` を単一のソースとする `data/*.yml` へ移行した。

あわせて分類を整理した。生成される README の内容が変わる。

- プログラミング言語は言語をフラットに列挙し、関連パッケージ・ツールを言語ごとに分けた
- `SQL` を追加した
- `Terraform` はツール類（IaC）へ移し、言語としては `HCL` を置いた
- `Deep Learning` / `ML` の分野まとめを解消し、`etc...` を廃止した
- 実績の `[記事削除済]` を `deleted` フラグにした
- 英語の見出しを `Language` から `Languages` に直した
