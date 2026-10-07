# キャッチゲーム - 環境構築手順

## 【中級コース】Python + Pygame版

---

## 必要なもの

```
□ Python 3.8以上
□ テキストエディタ（VSCode推奨）
□ ターミナル/コマンドプロンプト
```

---

## セットアップ手順

### 📝 事前準備チェックリスト

```
□ Pythonがインストールされているか確認
□ pipが使えるか確認
□ テキストエディタがあるか確認
```

---

## ステップ1：Pythonのインストール確認

### Windows

```
1. コマンドプロンプトを開く
   - Windowsキー + R
   - 「cmd」と入力してEnter

2. 以下のコマンドを実行：
   python --version

3. 「Python 3.8.x」以上と表示されればOK

表示されない場合：
- Pythonをインストール必要
- https://www.python.org/downloads/
- 「Add Python to PATH」に必ずチェック
```

### Mac

```
1. ターミナルを開く
   - Spotlight（Command + Space）
   - 「ターミナル」と入力

2. 以下のコマンドを実行：
   python3 --version

3. 「Python 3.8.x」以上と表示されればOK

表示されない場合：
- Homebrewでインストール推奨
- brew install python3
```

---

## ステップ2：プロジェクトファイルの準備

### ダウンロード

```
1. GitHubまたは配布されたZIPファイルをダウンロード

2. 適当な場所に解凍
   例：デスクトップに「catch-game」フォルダ

3. ファイル確認：
   📁 catch-game
     📄 game.py（完成例）
     📄 game_template.py（テンプレート）
     📄 requirements.txt
```

---

## ステップ3：Pygameのインストール

### Windows

```
1. コマンドプロンプトを開く

2. プロジェクトフォルダに移動：
   cd デスクトップ\catch-game

3. Pygameをインストール：
   pip install pygame --break-system-packages

   または

   pip install -r requirements.txt --break-system-packages

4. 完了メッセージが表示されればOK
```

### Mac/Linux

```
1. ターミナルを開く

2. プロジェクトフォルダに移動：
   cd ~/Desktop/catch-game

3. Pygameをインストール：
   pip3 install pygame

   または

   pip3 install -r requirements.txt

4. 完了メッセージが表示されればOK
```

### インストール確認

```
1. Pythonインタラクティブシェルを起動：
   python（Windowsの場合）
   python3（Mac/Linuxの場合）

2. 以下を実行：
   import pygame
   print(pygame.version.ver)

3. バージョンが表示されれば成功
   例：2.5.2

4. 終了：
   exit()
```

---

## ステップ4：動作確認

### 完成例を実行

```
1. ターミナル/コマンドプロンプトで：
   python game.py（Windows）
   python3 game.py（Mac/Linux）

2. ゲームウィンドウが開く

3. ←→キーで左右移動

4. 落ちてくるアイテムをキャッチ

5. 動けば成功！

終了：
- ウィンドウの×ボタン
- または ESC キー（ゲームオーバー後）
```

---

## ステップ5：開発環境の準備

### VSCodeでの開発（推奨）

```
1. VSCodeを起動

2. 「ファイル」→「フォルダを開く」

3. catch-game フォルダを選択

4. game_template.py を開く

5. これで開発準備完了！
```

### Python拡張機能（推奨）

```
1. VSCodeの左側「拡張機能」アイコンをクリック

2. 「Python」と検索

3. Microsoft製の「Python」をインストール

メリット：
- シンタックスハイライト
- コード補完
- デバッグ機能
```

---

## 開発の始め方

### テンプレート版で開発

```
編集するファイル：
- game_template.py

手順：
1. TODO 1 から順番に実装
2. 定期的に実行して動作確認
3. エラーが出たら修正

実行方法：
python game_template.py（Windows）
python3 game_template.py（Mac/Linux）
```

### 完成例を参考に

```
参考ファイル：
- game.py

困ったら：
1. game.py を見る
2. 該当する部分を確認
3. 同じように書いてみる
```

---

## トラブルシューティング

### Q1: 「python: command not found」

```
原因：
- Pythonがインストールされていない
- PATHが通っていない

解決方法：
【Windows】
1. Pythonを再インストール
2. 「Add Python to PATH」にチェック

【Mac】
- python3 コマンドを使う
- または python → python3 のエイリアスを設定
```

### Q2: 「No module named 'pygame'」

```
原因：
- Pygameがインストールされていない

解決方法：
pip install pygame --break-system-packages（Windows）
pip3 install pygame（Mac/Linux）
```

### Q3: Pygameのウィンドウが開かない

```
原因：
- グラフィックドライバの問題
- Pygame初期化エラー

確認：
1. エラーメッセージを確認
2. Pythonのバージョン確認
3. Pygameを再インストール
```

### Q4: 実行すると即座に終了する

```
原因：
- 構文エラー
- インデントエラー

解決方法：
1. エラーメッセージを確認
2. 該当行のコードを確認
3. インデントをチェック（スペース4つ）
```

### Q5: アイテムが表示されない

```
原因：
- draw() 関数が未実装
- 色の定義が間違っている

確認：
1. TODO 11 を確認
2. pygame.draw.circle が正しく書かれているか
3. 色が定義されているか
```

### Q6: キー入力が効かない

```
原因：
- move() 関数が未実装

確認：
1. TODO 5 を確認
2. keys[pygame.K_LEFT] の処理が書かれているか
```

---

## よくあるエラーと対処法

### IndentationError

```
エラー：
  IndentationError: expected an indented block

原因：
- インデント（字下げ）が間違っている

解決：
- Pythonは字下げが重要
- 関数の中は4スペース字下げ
- タブとスペースを混在させない
```

### AttributeError

```
エラー：
  AttributeError: 'Player' object has no attribute 'x'

原因：
- __init__ で変数を定義していない

解決：
- TODO 4 を確認
- self.x = ... を追加
```

### TypeError

```
エラー：
  TypeError: 'NoneType' object is not subscriptable

原因：
- 関数が何も返していない
- return文が抜けている

解決：
- get_rect() など、return が必要な関数を確認
```

---

## 当日の流れ

```
14:00-14:20 環境確認・セットアップ
  - Pythonインストール確認
  - Pygameインストール
  - 動作確認

14:20-14:30 デモ・説明
  - 完成例を見る
  - Pygameの基礎説明

14:30-16:45 開発タイム
  - game_template.py の TODO を順番に実装
  - 定期的に実行して確認
  - エラーが出たらデバッグ
  - 分からなければサポート役に質問

16:45-17:00 発表
```

---

## 事前準備（強く推奨）

当日スムーズに始めるために、**必ず事前に以下をやっておいてください**：

```
□ Python 3.8以上をインストール
□ pipが使えることを確認
□ Pygameをインストール
□ 完成例（game.py）を実行して動作確認
□ VSCodeをインストール（推奨）
□ Python拡張機能をインストール（推奨）
```

**特に重要：**
- Pygameのインストールは事前に！
- 当日ネットワークが混むと時間がかかります

---

## 推奨スペック

```
OS：
- Windows 10/11
- macOS 10.15以降
- Ubuntu 20.04以降

メモリ：
- 4GB以上

Python：
- 3.8以上
```

---

## 参考リンク

```
- Python公式: https://www.python.org/
- Pygame公式: https://www.pygame.org/
- VSCode: https://code.visualstudio.com/
- Pygameドキュメント: https://www.pygame.org/docs/
```

---

## セットアップ確認チェックリスト

当日までに以下を確認：

```
□ python --version でバージョン表示される
□ pip --version でバージョン表示される
□ pip install pygame が成功する
□ python game.py でゲームが起動する
□ ←→キーで移動できる
□ アイテムが落ちてくる
```

**全てOKなら準備完了です！**

---

## 困ったら

当日、分からないことがあれば遠慮なく質問してください！
特に環境構築でつまずいたら、すぐにサポート役を呼んでください。

**一緒に楽しく開発しましょう！🎮**
