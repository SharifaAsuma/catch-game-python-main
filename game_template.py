"""
キャッチゲーム - テンプレート版
Python + Pygame

落ちてくるアイテムをキャッチしてスコアを稼ぐゲーム
"""

import pygame
import random
import sys

# TODO 1: Pygameの初期化
pygame.init()


# TODO 2: 画面設定
# 幅800、高さ600のウィンドウを作成
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("キャッチゲーム")


# TODO 3: 色定義
# 以下の色を定義してください（RGB形式）
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE = (70, 130, 180)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
GREEN = (50, 205, 50)


# ゲーム設定
FPS = 60
GAME_TIME = 60


class Player:
    """プレイヤークラス"""
    
    def __init__(self):
        # TODO 4: プレイヤーの初期設定
        # 幅80、高さ80、画面中央下に配置
        self.width = 80
        self.height = 80
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 100
        self.speed = 8
        pass
    
    def move(self, direction):
        """左右移動"""
        # TODO 5: 左右移動の実装（画面外に出ないように）
        # ヒント: if direction == "LEFT" and self.x > 0:
        #            self.x -= self.speed
        pass
    
    def draw(self, screen):
        """プレイヤー描画"""
        # TODO 6: 青い四角を描画
        # ヒント: pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        #        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 3)
        pass
    
    def get_rect(self):
        """当たり判定用の矩形"""
        # TODO 7: Rectオブジェクトを返す
        # ヒント: return pygame.Rect(self.x, self.y, self.width, self.height)
        pass


class Item:
    """アイテムクラス"""
    
    def __init__(self, item_type):
        self.type = item_type
        self.radius = 20
        # TODO 8: アイテムの初期位置（ランダムなX座標、Y座標は画面外上部）
        # ヒント: self.x = random.randint(self.radius, WIDTH - self.radius)
        #        self.y = -self.radius
        
        self.speed = 5
        
        # TODO 9: アイテムごとの色と得点を設定
        # リンゴ（赤）: +10点
        # バナナ（黄）: +15点
        # スイカ（緑）: +20点
        # 爆弾（黒）: -15点
        # ヒント: if item_type == 'apple':
        #            self.color = RED
        #            self.points = 10
        
    
    def fall(self):
        """落下処理"""
        # TODO 10: Y座標を増やして落下させる
        # ヒント: self.y += self.speed
        pass
    
    def draw(self, screen):
        """アイテム描画"""
        # TODO 11: 円を描画
        # ヒント: pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        #        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 2)
        pass
    
    def is_caught(self, player):
        """衝突判定"""
        # TODO 12: プレイヤーとの衝突判定
        # プレイヤーの矩形を取得して、アイテムの座標が範囲内か確認
        # ヒント: player_rect = player.get_rect()
        #        if (player_rect.left <= self.x <= player_rect.right and
        #            player_rect.top <= self.y <= player_rect.bottom):
        #            return True
        #        return False
        pass
    
    def is_off_screen(self):
        """画面外判定"""
        # TODO 13: 画面下に出たか確認
        # ヒント: return self.y > HEIGHT + self.radius
        pass


def main():
    """メインゲームループ"""
    # TODO 14: クロックオブジェクト作成
    # ヒント: clock = pygame.time.Clock()
    
    
    # TODO 15: ゲーム変数の初期化
    # player, items, score, time_left, frame_count, game_over
    # ヒント: player = Player()
    #        items = []
    #        score = 0
    #        time_left = GAME_TIME
    
    
    # フォント
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        # TODO 16: FPSを設定
        # ヒント: clock.tick(FPS)
        
        
        # TODO 17: イベント処理（ウィンドウを閉じる）
        # ヒント: for event in pygame.event.get():
        #            if event.type == pygame.QUIT:
        #                running = False
        
        
        if not game_over:
            # TODO 18: キー入力取得と移動
            # ← キーで左移動、→ キーで右移動
            # ヒント: keys = pygame.key.get_pressed()
            #        if keys[pygame.K_LEFT]:
            #            player.move("LEFT")
            
            
            # TODO 19: アイテム生成（1.5秒ごと = 90フレーム）
            # 70%で良いアイテム、30%で爆弾
            # ヒント: if frame_count % 90 == 0 and len(items) < 3:
            #            if random.random() < 0.7:
            #                item_type = random.choice(['apple', 'banana', 'watermelon'])
            #            else:
            #                item_type = 'bomb'
            #            items.append(Item(item_type))
            
            
            # TODO 20: アイテム更新（落下、衝突判定、画面外判定）
            # ヒント: for item in items[:]:
            #            item.fall()
            #            if item.is_caught(player):
            #                score += item.points
            #                items.remove(item)
            #            elif item.is_off_screen():
            #                items.remove(item)
            
            
            # TODO 21: タイマー更新（60フレーム = 1秒）
            # ヒント: frame_count += 1
            #        if frame_count >= FPS:
            #            frame_count = 0
            #            time_left -= 1
            #            if time_left <= 0:
            #                game_over = True
            
        
        # TODO 22: 画面を塗りつぶす
        # ヒント: screen.fill(GRAY)
        
        
        # TODO 23: プレイヤーを描画
        # ヒント: player.draw(screen)
        
        
        # TODO 24: アイテムを描画
        # ヒント: for item in items:
        #            item.draw(screen)
        
        
        # TODO 25: スコアとタイマーを表示
        # ヒント: score_text = font.render(f"Score: {score}", True, BLACK)
        #        screen.blit(score_text, (10, 10))
        
        
        # TODO 26: ゲームオーバー時の表示
        # ヒント: if game_over:
        #            ... (ゲームオーバー画面の描画)
        
        
        # TODO 27: 画面を更新
        # ヒント: pygame.display.flip()
        
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
