---
type: Convention
title: URL の持ち方
description: URL をインラインで持つ規約。
tags: [links, url]
timestamp: 2026-08-16T00:00:00Z
---

URL は項目の `url` に直接書く。参照用の登録簿は設けない。

```yaml
- name: Tableau
  url: https://www.tableau.com/
```

文章の途中に現れるリンクは Markdown 記法のまま値に含める。

```yaml
- name: "[DATA Saber](https://datasaber.world/) a.k.a. Trickstar"
```

登録簿方式を検討したが、2 回以上参照される URL が 123 件中 32 件しかなく、
`[Tableau][tableau]` のように同じ名前を 2 度書く重複を 29 件生むだけだったため採用しなかった。

# 関連

- [記述規約](index.md)
- [ファイル一覧](../files/index.md)
