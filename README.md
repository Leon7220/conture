# 視聴・プレイ記録リマインダー（Flask CRUD App）

アニメ・ゲームなどの視聴／プレイ履歴を記録・管理するための  
シンプルな CRUD Web アプリケーションです。

Flask + SQLite3 を用いて実装しています。

---

## 機能概要

- 作品の追加（Create）
- 作品一覧の表示（Read）
- 作品情報の編集（Update）
- 作品の削除（Delete）
- 評価は ★1?★5 の5段階評価
- 状態管理（todo / doing / done）

---

## 使用技術

- Python 3.x
- Flask
- SQLite3
- HTML / CSS (Jinja2)

---

## ディレクトリ構成
.
├── app.py
├── contents.db # 初回起動時に自動生成
├── requirements.txt
├── README.md
├── static/
│ └── style.css
└── templates/
├── index.html
├── add.html
└── edit.html


---

## セットアップ手順

### 1. リポジトリをクローン

```bash
git clone <GitHubリポジトリURL>
cd <リポジトリ名>
### 2．仮想環境(任意)
python -m venv venv
source venv/bin/activate   # Windowsは venv\Scripts\activate
### 3. ライブラリのインストール
pip install -r requirements.txt

## データベースについて
SQLite3 を使用

app.py 起動時に以下のテーブルが自動作成されます

CREATE TABLE contents (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  type TEXT,
  status TEXT,
  rating INTEGER,
  comment TEXT
);
※ 事前に DB を作成する必要はありません。

##アプリケーションの起動方法
python app.py
ブラウザで以下にアクセス
http://127.0.0.1:5000/



## データベース初期化手順

本アプリケーションでは SQLite を使用しています。
特別な DB 作成コマンドは不要で、アプリ起動時に自動で初期化されます。

### 使用DB
- SQLite
- DBファイル名：`contents.db`

### 初期化方法

##1. 必要なライブラリをインストールします。

```bash
pip install -r requirements.txt

##2. Flask アプリを起動します。
python app.py

##3. 初回起動時に以下のテーブルが自動で作成されます。
CREATE TABLE contents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    type TEXT,
    status TEXT,
    rating INTEGER,
    comment TEXT
);

##4. ブラウザで以下にアクセスします。
http://127.0.0.1:5000
