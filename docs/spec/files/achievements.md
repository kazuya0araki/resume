---
type: Schema
title: data/achievements.yml
description: 登壇・メディア掲載・著書。
resource: https://github.com/kazuya0araki/resume/blob/main/data/achievements.yml
tags: [schema, achievements]
timestamp: 2026-08-16T00:00:00Z
---

登壇・メディア掲載・著書。

対応する章は「実績」。

# スキーマ

キーは実データから導出している。`[]` は配列の要素を表す。

| キー | 型 | 必須 | 説明 | 実例 |
|---|---|---|---|---|
| `title` | 文字列（対訳） | ○ |  | 実績 |
| `talks.title` | 文字列（対訳） | ○ |  | 登壇 |
| `talks.items[].date` | 日付（YYYY-MM-DD） | ○ | 実施日（YYYY-MM-DD）。 | 2018-09-26 |
| `talks.items[].title` | 文字列（対訳） | ○ |  | Data Peopleの為の勉強会 \~Eureka×Leverages×B… |
| `talks.items[].url` | URL |  |  | https://data-analyst.connpass.com/even… |
| `talks.items[].material` | 文字列（対訳） |  | 発表資料の名称。 | 株式会社ビズリーチの紹介@Data Analyst Meetup Tokyo… |
| `talks.items[].material_url` | URL |  |  | https://speakerdeck.com/kazuya_araki_t… |
| `media.title` | 文字列（対訳） | ○ |  | メディア、ブログ掲載 |
| `media.items[].date` | 日付（YYYY-MM-DD） | ○ |  | 2018-07-18 |
| `media.items[].title` | 文字列（対訳） | ○ |  | データの力で、事業を加速する｜BIグループの仕事を公開！ |
| `media.items[].url` | URL | ○ |  | https://reachone.bizreach.co.jp/entry/… |
| `media.items[].deleted` | 真偽値 |  | true のとき、生成時にタイトルへ「[記事削除済]」を付ける。 | true |
| `books.title` | 文字列（対訳） | ○ |  | 著書 |
| `books.items[].date` | 日付（YYYY-MM-DD） | ○ |  | 2022-03-01 |
| `books.items[].title` | 文字列 | ○ |  | 動き出すデータドリブン組織のつくりかた Tableau Blueprintに… |
| `books.items[].url` | URL | ○ |  | https://amzn.to/3gOvJC9 |

# 関連

- [記述規約](../conventions/index.md)
- [ファイル一覧](index.md)
