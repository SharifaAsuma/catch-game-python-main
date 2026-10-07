# キャッチゲーム - 開発マニュアル

## 【中級コース】ステップバイステップガイド

---

## 🎯 完成目標

```
60秒間で、上から落ちてくるアイテムをキャッチしてスコアを稼ぐゲーム

機能：
✅ プレイヤーを←→キーで左右移動
✅ アイテムが上から落ちてくる
✅ 良いアイテム（リンゴ、バナナ、スイカ）
✅ 悪いアイテム（爆弾）
✅ 衝突判定
✅ 60秒のタイマー
✅ 結果表示
```

---

## 📝 開発の流れ

```
全6ステップ、約3時間で完成！

ステップ1: Pygame基礎設定      （20分）
ステップ2: プレイヤー移動      （25分）
ステップ3: アイテム落下        （30分）
ステップ4: 衝突判定            （25分）
ステップ5: スコア・タイマー    （25分）
ステップ6: ゲーム終了処理      （20分）
```

---

## ステップ1：Pygame基礎設定（20分）

### 🎯 目標

Pygameウィンドウが開き、空の画面が表示される

### 📋 やること

`game_template.py` の基本設定を実装します。

```python
# TODO 1-3 を実装

# TODO 1: Pygameの初期化
import pygame
import random
import sys

pygame.init()

# TODO 2: 画面設定
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("キャッチゲーム")

# TODO 3: 色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE = (70, 130, 180)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
GREEN = (50, 205, 50)
```

### ✅ 動作確認

```
1. ターミナルで実行：
   python game_template.py

2. ウィンドウが開く

3. グレーの画面が表示される

4. ×ボタンで閉じられる

→ 基礎設定完了！
```

### 💡 ポイント

```
Pygameの初期化：
- pygame.init() は必須
- 最初に1回だけ呼ぶ

画面の作成：
- set_mode((幅, 高さ))
- タプル形式で指定

色の定義：
- RGB形式：(赤, 緑, 青)
- 各0-255の値
- 例：(255, 0, 0) = 赤
```

### ❌ よくあるミス

```
ミス1: init() を忘れる
× # pygame.init() なし  ❌
○ pygame.init()         ✅

ミス2: タプルの括弧ミス
× set_mode(WIDTH, HEIGHT)  ❌
○ set_mode((WIDTH, HEIGHT)) ✅（二重括弧）

ミス3: 色の値が範囲外
× RED = (300, 0, 0)  ❌（最大255）
○ RED = (255, 0, 0)  ✅
```

---

## ステップ2：プレイヤー移動（25分）

### 🎯 目標

青い四角（プレイヤー）が←→キーで左右に動く

### 📋 やること

`Player` クラスを実装します。

```python
# TODO 4-7 を実装

class Player:
    def __init__(self):
        # TODO 4: プレイヤーの初期設定
        self.width = 80
        self.height = 80
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 100
        self.speed = 8
    
    def move(self, direction):
        # TODO 5: 左右移動の実装
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < WIDTH - self.width:
            self.x += self.speed
    
    def draw(self, screen):
        # TODO 6: プレイヤー描画
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 3)
    
    def get_rect(self):
        # TODO 7: Rectオブジェクトを返す
        return pygame.Rect(self.x, self.y, self.width, self.height)
```

### メインループでの使用

```python
# TODO 14, 18 を実装

# main() 関数内
player = Player()

# メインループ内
# TODO 18: キー入力取得と移動
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:
    player.move("LEFT")
if keys[pygame.K_RIGHT]:
    player.move("RIGHT")

# TODO 23: プレイヤーを描画
player.draw(screen)
```

### ✅ 動作確認

```
1. 実行する
2. 青い四角が画面下に表示される
3. ←キーを押すと左に動く
4. →キーを押すと右に動く
5. 画面外に出ない

→ プレイヤー移動完了！
```

### 💡 ポイント

```
クラスの使い方：
class Player:
    def __init__(self):
        # 初期化
        self.x = 100
    
    def move(self):
        # メソッド
        self.x += 1

pygame.draw.rect の使い方：
pygame.draw.rect(
    screen,          # 描画先
    BLUE,           # 色
    (x, y, w, h),   # 矩形（x座標, y座標, 幅, 高さ）
    3               # 線の太さ（省略で塗りつぶし）
)

キー入力の取得：
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:  # ←キー
if keys[pygame.K_RIGHT]: # →キー
```

### ❌ よくあるミス

```
ミス1: self を忘れる
× def __init__():      ❌
○ def __init__(self):  ✅

× x = 100              ❌
○ self.x = 100         ✅

ミス2: インデントミス
× def move(self):
    self.x += 1        ❌（インデントなし）
○ def move(self):
      self.x += 1      ✅（4スペース）

ミス3: 画面外判定のミス
× if self.x < WIDTH:   ❌（右端で止まらない）
○ if self.x < WIDTH - self.width: ✅
```

---

## ステップ3：アイテム落下（30分）

### 🎯 目標

上から色付きの円（アイテム）が落ちてくる

### 📋 やること

`Item` クラスを実装します。

```python
# TODO 8-13 を実装

class Item:
    def __init__(self, item_type):
        self.type = item_type
        self.radius = 20
        
        # TODO 8: アイテムの初期位置
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = -self.radius
        self.speed = 5
        
        # TODO 9: アイテムごとの色と得点を設定
        if item_type == 'apple':
            self.color = RED
            self.points = 10
        elif item_type == 'banana':
            self.color = YELLOW
            self.points = 15
        elif item_type == 'watermelon':
            self.color = GREEN
            self.points = 20
        elif item_type == 'bomb':
            self.color = BLACK
            self.points = -15
    
    def fall(self):
        # TODO 10: Y座標を増やして落下させる
        self.y += self.speed
    
    def draw(self, screen):
        # TODO 11: 円を描画
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 2)
    
    def is_caught(self, player):
        # TODO 12: プレイヤーとの衝突判定
        player_rect = player.get_rect()
        if (player_rect.left <= self.x <= player_rect.right and
            player_rect.top <= self.y <= player_rect.bottom):
            return True
        return False
    
    def is_off_screen(self):
        # TODO 13: 画面外判定
        return self.y > HEIGHT + self.radius
```

### メインループでの使用

```python
# TODO 19, 20, 24 を実装

# main() 関数内
items = []
frame_count = 0

# メインループ内
# TODO 19: アイテム生成
frame_count += 1
if frame_count >= 90:  # 1.5秒ごと
    frame_count = 0
    if len(items) < 3:  # 最大3個
        if random.random() < 0.7:  # 70%で良いアイテム
            item_type = random.choice(['apple', 'banana', 'watermelon'])
        else:  # 30%で爆弾
            item_type = 'bomb'
        items.append(Item(item_type))

# TODO 20: アイテム更新
for item in items[:]:
    item.fall()
    if item.is_caught(player):
        score += item.points
        items.remove(item)
    elif item.is_off_screen():
        items.remove(item)

# TODO 24: アイテムを描画
for item in items:
    item.draw(screen)
```

### ✅ 動作確認

```
1. 実行する
2. 色付きの円が上から落ちてくる
3. 画面下まで落ちると消える
4. 定期的に新しいアイテムが出現

→ アイテム落下完了！
```

### 💡 ポイント

```
random.randint の使い方：
random.randint(a, b)  # a以上b以下の整数
例：random.randint(0, 100)  # 0～100

pygame.draw.circle の使い方：
pygame.draw.circle(
    screen,        # 描画先
    RED,          # 色
    (x, y),       # 中心座標
    radius,       # 半径
    2             # 線の太さ（省略で塗りつぶし）
)

リストのコピー：
for item in items[:]:  # コピーを作ってループ
    items.remove(item)  # 元のリストから削除OK

× for item in items:   # 直接ループ
    items.remove(item) # エラーになる可能性
```

### ❌ よくあるミス

```
ミス1: タプルの括弧忘れ
× pygame.draw.circle(screen, RED, self.x, self.y, self.radius)  ❌
○ pygame.draw.circle(screen, RED, (self.x, self.y), self.radius) ✅

ミス2: int() 変換を忘れる
× (self.x, self.y)  ❌（小数の場合エラー）
○ (int(self.x), int(self.y))  ✅

ミス3: ループ中のリスト削除
× for item in items:
    items.remove(item)  ❌
○ for item in items[:]:
    items.remove(item)  ✅
```

---

## ステップ4：衝突判定（25分）

### 🎯 目標

プレイヤーがアイテムをキャッチしたらスコアが変わる

### 📋 やること

ステップ3のTODO 12で既に実装していますが、確認しましょう。

```python
def is_caught(self, player):
    # プレイヤーの矩形を取得
    player_rect = player.get_rect()
    
    # アイテムの中心がプレイヤーの範囲内にあるか
    if (player_rect.left <= self.x <= player_rect.right and
        player_rect.top <= self.y <= player_rect.bottom):
        return True
    return False
```

### メインループでの使用

```python
# アイテム更新ループ内
for item in items[:]:
    item.fall()
    
    # 衝突判定
    if item.is_caught(player):
        score += item.points  # スコア加算
        items.remove(item)    # アイテム削除
    elif item.is_off_screen():
        items.remove(item)
```

### ✅ 動作確認

```
1. 実行する
2. プレイヤーを動かす
3. 落ちてくるアイテムをキャッチ
4. スコアが変わる：
   - 赤（リンゴ）: +10
   - 黄（バナナ）: +15
   - 緑（スイカ）: +20
   - 黒（爆弾）: -15

→ 衝突判定完了！
```

### 💡 ポイント

```
矩形の当たり判定：
player_rect = pygame.Rect(x, y, width, height)
- left: 左端のX座標
- right: 右端のX座標
- top: 上端のY座標
- bottom: 下端のY座標

円と矩形の当たり判定（簡易版）：
- 円の中心が矩形内にあるか確認
- 正確ではないが、ゲームとしては十分
```

### ❌ よくあるミス

```
ミス1: <= と < の混同
× if player_rect.left < self.x < player_rect.right:  ❌
○ if player_rect.left <= self.x <= player_rect.right: ✅

ミス2: and と or の混同
× if (x条件 or y条件):  ❌（どちらか1つで判定）
○ if (x条件 and y条件): ✅（両方必要）

ミス3: 削除のタイミング
× item.fall()
  items.remove(item)  ❌（常に削除）
  if item.is_caught(player):
    score += item.points

○ item.fall()
  if item.is_caught(player):
    score += item.points
    items.remove(item)  ✅
```

---

## ステップ5：スコア・タイマー管理（25分）

### 🎯 目標

スコアとタイマーが画面に表示され、時間が減っていく

### 📋 やること

```python
# TODO 15, 21, 25 を実装

# main() 関数内
score = 0
time_left = GAME_TIME  # 60秒
frame_count = 0
font = pygame.font.Font(None, 36)

# メインループ内
# TODO 21: タイマー更新
frame_count += 1
if frame_count >= FPS:  # 60フレーム = 1秒
    frame_count = 0
    time_left -= 1
    if time_left <= 0:
        game_over = True

# TODO 22: 画面を塗りつぶす
screen.fill(GRAY)

# TODO 25: スコアとタイマーを表示
score_text = font.render(f"Score: {score}", True, BLACK)
screen.blit(score_text, (10, 10))

time_text = font.render(f"Time: {time_left}", True, BLACK)
screen.blit(time_text, (WIDTH - 150, 10))
```

### ✅ 動作確認

```
1. 実行する
2. 左上に「Score: 0」が表示される
3. 右上に「Time: 60」が表示される
4. 1秒ごとに時間が減る
5. アイテムをキャッチするとスコアが変わる

→ スコア・タイマー完了！
```

### 💡 ポイント

```
フォントの使い方：
font = pygame.font.Font(None, サイズ)
# None = デフォルトフォント

テキストの描画：
text = font.render("文字列", True, 色)
screen.blit(text, (x, y))

フレームとタイマーの関係：
- FPS = 60（1秒間に60フレーム）
- 60フレーム = 1秒
- frame_count >= 60 で1秒経過
```

### ❌ よくあるミス

```
ミス1: f-string の書き方ミス
× f"Score: {score}"   ❌（クォートミス）
○ f"Score: {score}"   ✅（fと"の間にスペースなし）

ミス2: blit の座標ミス
× screen.blit(text, 10, 10)  ❌
○ screen.blit(text, (10, 10)) ✅（タプル）

ミス3: fill を忘れる
× # screen.fill(GRAY) なし  ❌
○ screen.fill(GRAY)          ✅
```

---

## ステップ6：ゲーム終了処理（20分）

### 🎯 目標

60秒経過したら、ゲームオーバー画面を表示

### 📋 やること

```python
# TODO 26, 27 を実装

# main() 関数内
game_over = False
font_large = pygame.font.Font(None, 48)

# メインループ内
# TODO 26: ゲームオーバー時の表示
if game_over:
    # 半透明の背景
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(WHITE)
    screen.blit(overlay, (0, 0))
    
    # ゲームオーバーテキスト
    game_over_text = font_large.render("GAME OVER", True, BLACK)
    game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    screen.blit(game_over_text, game_over_rect)
    
    # 最終スコア
    score_text = font.render(f"Final Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
    screen.blit(score_text, score_rect)
    
    # 終了案内
    restart_text = font.render("Press ESC to exit", True, BLACK)
    restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 70))
    screen.blit(restart_text, restart_rect)
    
    # ESCキーで終了
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

# TODO 27: 画面を更新
pygame.display.flip()
```

### ✅ 動作確認

```
1. 実行する
2. 60秒待つ
3. 「GAME OVER」画面が表示される
4. 最終スコアが表示される
5. ESCキーで終了できる

→ ゲーム終了処理完了！
```

### 💡 ポイント

```
半透明の背景の作り方：
overlay = pygame.Surface((WIDTH, HEIGHT))
overlay.set_alpha(200)  # 0(透明)～255(不透明)
overlay.fill(WHITE)
screen.blit(overlay, (0, 0))

テキストの中央配置：
text = font.render("文字列", True, BLACK)
rect = text.get_rect(center=(x, y))
screen.blit(text, rect)

画面更新：
pygame.display.flip()  # 全体を更新
または
pygame.display.update()  # 部分的に更新
```

### ❌ よくあるミス

```
ミス1: flip() を忘れる
× # pygame.display.flip() なし  ❌
○ pygame.display.flip()          ✅

ミス2: get_rect のパラメータミス
× get_rect((WIDTH//2, HEIGHT//2))  ❌
○ get_rect(center=(WIDTH//2, HEIGHT//2)) ✅

ミス3: alpha の値が間違い
× overlay.set_alpha(255)  ❌（完全に不透明）
○ overlay.set_alpha(200)  ✅（半透明）
```

---

## 🎉 完成！

全てのステップが完了したら、以下を確認：

```
✅ ゲームウィンドウが開く
✅ プレイヤーが←→で動く
✅ アイテムが落ちてくる
✅ キャッチするとスコアが変わる
✅ タイマーが60秒からカウントダウン
✅ 0秒でゲームオーバー画面
```

**おめでとうございます！🎮**

---

## 🚀 カスタマイズアイデア

### レベル1：簡単

```
□ ゲーム時間を変更（30秒、90秒など）
□ アイテムの落下速度を変更
□ プレイヤーの速度を変更
□ アイテムの得点を変更
```

### レベル2：中級

```
□ ハイスコアを記録
□ 難易度選択
□ アイテムの種類を増やす
□ 背景画像を追加
□ 効果音を追加
```

### レベル3：上級

```
□ レベルアップ機能（時間経過で速くなる）
□ パワーアップアイテム（時間延長、2倍得点など）
□ ライフ制（爆弾で減る）
□ アニメーション（アイテムが回転）
□ スコアランキング保存
```

---

## 📚 参考：Pygameの基本

### 基本構造

```python
import pygame
pygame.init()

# 設定
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# メインループ
running = True
while running:
    clock.tick(FPS)  # フレームレート制御
    
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 更新処理
    
    # 描画処理
    screen.fill(WHITE)
    # ...描画...
    pygame.display.flip()

pygame.quit()
```

### 描画関数

```python
# 矩形
pygame.draw.rect(screen, color, (x, y, w, h))

# 円
pygame.draw.circle(screen, color, (x, y), radius)

# 線
pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)
```

### キー入力

```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]:   # ←
if keys[pygame.K_RIGHT]:  # →
if keys[pygame.K_UP]:     # ↑
if keys[pygame.K_DOWN]:   # ↓
if keys[pygame.K_SPACE]:  # スペース
```

---

## ❓ よくある質問

### Q1: ウィンドウが開かない

```
確認：
□ pygame.init() を実行したか
□ screen = pygame.display.set_mode(...) を実行したか
□ メインループがあるか
```

### Q2: アイテムが表示されない

```
確認：
□ draw() メソッドを実装したか
□ for item in items: item.draw(screen) を書いたか
□ pygame.display.flip() を呼んでいるか
```

### Q3: キー入力が効かない

```
確認：
□ keys = pygame.key.get_pressed() を書いたか
□ if keys[pygame.K_LEFT]: の処理があるか
□ player.move() を呼んでいるか
```

### Q4: エラー: IndentationError

```
原因：
- インデント（字下げ）が間違っている

解決：
- Pythonは字下げが重要
- 4スペースで統一
- タブとスペースを混在させない
```

---

## 🎯 完成のコツ

```
1. 一度に全部やろうとしない
   → ステップごとに実行して確認

2. エラーメッセージをよく読む
   → どの行でエラーが出ているか確認

3. print() でデバッグ
   → 変数の値を表示して確認

4. 完成例を参考にする
   → 理解しながら見る

5. 楽しむ！
   → 一番大事です
```

---

**頑張ってください！応援しています！🎮**
