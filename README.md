# first-calender
技術を学びつつ，就活で「こんなん作ったっていえたらいいね」ってやつ

## 概要
GoogleカレンダーのようなカレンダーUIに予定を登録して，視覚的に管理するWebアプリ

## 開発環境

### バックエンド
- MySQL
- net/http,
- gorm?(未定)

### フロントエンド
Nuxt.js
- axios(非同期処理)

### その他
docker
- MySQLコンテナ
- GolangのAPIサーバ

## あったらいいな機能案
- 使用頻度に基づくリマインドの調整機能
ユーザがアプリを使用する頻度でアプリ側が書くスケジュールに重要度を与えて，リマインドのタイミングを調整する

- 予定の名前から自動的に予定の色が付加される
予定の名前の入力と色の指定の２度手間を省略できる

- firebase等を用いたログイン機能 