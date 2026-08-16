---
type: Convention
title: リストの持ち方
description: 入れ子の帰属を曖昧にしないための規約。
tags: [lists, nesting]
timestamp: 2026-08-16T00:00:00Z
---

リストの要素は**すべて `- name:` で始める**。文字列と入れ子を同じ配列に混在させない。

```yaml
items:
  - name: pip
  - name: Node.js
    items:
      - name: Express
```

混在させると、どの項目に子がぶら下がっているかを読み違える。
実際に検討中、6 行の抜粋で誤読が起きたため、この規約を設けた。

入れ子は実体としての従属関係がある場合にだけ使う。
「Deep Learning」のような分野によるまとめは、区分の見出しで表す。

# 関連

- [記述規約](index.md)
- [ファイル一覧](../files/index.md)
