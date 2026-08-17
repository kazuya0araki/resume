---
type: Schema
title: data/meta.yml
description: 更新日・対応言語・章の並び・生成時に使う固定語彙。
resource: https://github.com/kazuya0araki/resume/blob/main/data/meta.yml
tags: [schema, meta]
timestamp: 2026-08-16T00:00:00Z
---

更新日・対応言語・章の並び・生成時に使う固定語彙。

対応する章は「全体設定」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `updated` | 日付（YYYY-MM-DD） | ○ | 職務経歴書の基準日。生成物の「◯年◯月◯日現在」に使う。 | 2026-07-01 |
| `languages[]` | 文字列 | ○ |  | ja |
| `sections[]` | 文字列 | ○ |  | basic |
| `labels.ja.doc_title` | 文字列 | ○ |  | 職務経歴書 |
| `labels.ja.as_of` | 文字列 | ○ |  | *%s*現在 |
| `labels.ja.other_lang` | 文字列 | ○ |  | 英語版職務経歴書はこちら |
| `labels.ja.now` | 文字列 | ○ |  | 現在 |
| `labels.ja.basic` | 文字列 | ○ |  | 基本情報 |
| `labels.ja.name` | 文字列 | ○ |  | 氏名 |
| `labels.ja.birth` | 文字列 | ○ |  | 生年月日 |
| `labels.ja.sex` | 文字列 | ○ |  | 性別 |
| `labels.ja.residence` | 文字列 | ○ |  | 居住地 |
| `labels.ja.sns` | 文字列 | ○ |  | SNS etc. |
| `labels.ja.career` | 文字列 | ○ |  | 職務経歴 |
| `labels.ja.overview` | 文字列 | ○ |  | 概要 |
| `labels.ja.detail` | 文字列 | ○ |  | 詳細 |
| `labels.ja.th_term` | 文字列 | ○ |  | 在籍期間 |
| `labels.ja.th_company` | 文字列 | ○ |  | 社名 |
| `labels.ja.th_period` | 文字列 | ○ |  | 期間 |
| `labels.ja.th_org` | 文字列 | ○ |  | 所属組織 |
| `labels.ja.th_role` | 文字列 | ○ |  | 職位 |
| `labels.ja.th_content` | 文字列 | ○ |  | 内容 |
| `labels.ja.th_date` | 文字列 | ○ |  | 日付 |
| `labels.ja.th_title` | 文字列 | ○ |  | タイトル |
| `labels.ja.th_material` | 文字列 | ○ |  | 資料等 |
| `labels.ja.deleted` | 文字列 | ○ |  | [記事削除済] |
| `labels.en.doc_title` | 文字列 | ○ |  | Resume |
| `labels.en.as_of` | 文字列 | ○ |  | Since *%s* |
| `labels.en.other_lang` | 文字列 | ○ |  | Japanese Resume is here. |
| `labels.en.now` | 文字列 | ○ |  | Currently |
| `labels.en.basic` | 文字列 | ○ |  | Basic Information |
| `labels.en.name` | 文字列 | ○ |  | Full Name |
| `labels.en.birth` | 文字列 | ○ |  | Date of Birth |
| `labels.en.sex` | 文字列 | ○ |  | Sex |
| `labels.en.residence` | 文字列 | ○ |  | Residence |
| `labels.en.sns` | 文字列 | ○ |  | SNS etc. |
| `labels.en.career` | 文字列 | ○ |  | Job History |
| `labels.en.overview` | 文字列 | ○ |  | Overview |
| `labels.en.detail` | 文字列 | ○ |  | Detail |
| `labels.en.th_term` | 文字列 | ○ |  | Term |
| `labels.en.th_company` | 文字列 | ○ |  | Company |
| `labels.en.th_period` | 文字列 | ○ |  | Term |
| `labels.en.th_org` | 文字列 | ○ |  | Organization |
| `labels.en.th_role` | 文字列 | ○ |  | Role |
| `labels.en.th_content` | 文字列 | ○ |  | Contents |
| `labels.en.th_date` | 文字列 | ○ |  | Date |
| `labels.en.th_title` | 文字列 | ○ |  | Title |
| `labels.en.th_material` | 文字列 | ○ |  | References |
| `labels.en.deleted` | 文字列 | ○ |  | [Deleted] |

# 備考

`labels` は生成物にだけ現れる語彙で、データそのものではない。
表記ゆれを 1 箇所に閉じ込めるために置いている。

`sections` は章の出力順。ここに無い章は出力されない。

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
