"""
キャッチゲーム - 完成版
Python + Pygame

落ちてくるアイテムをキャッチしてスコアを稼ぐゲーム
"""

import pygame
import random
import sys

# Pygameの初期化
pygame.init()

# 画面設定
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("キャッチゲーム")

# 色定義（シンプル）
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
BLUE = (70, 130, 180)
RED = (220, 20, 60)
YELLOW = (255, 215, 0)
GREEN = (50, 205, 50)

# ゲーム設定
FPS = 60
GAME_TIME = 60  # 秒
ITEM_SPAWN_INTERVAL = 90  # フレーム（1.5秒）


class Player:
    """プレイヤークラス"""
    
    def __init__(self):
        self.width = 80
        self.height = 80
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 100
        self.speed = 8
    
    def move(self, direction):
        """左右移動（画面内に制限）"""
        if direction == "LEFT" and self.x > 0:
            self.x -= self.speed
        elif direction == "RIGHT" and self.x < WIDTH - self.width:
            self.x += self.speed
    
    def draw(self, screen):
        """プレイヤー描画（青い四角）"""
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 3)
    
    def get_rect(self):
        """当たり判定用の矩形を取得"""
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Item:
    """アイテムクラス"""
    
    def __init__(self, item_type):
        self.type = item_type
        self.radius = 20
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = -self.radius
        self.speed = 5
        
        # アイテムごとの設定
        if item_type == 'apple':
            self.color = RED
            self.points = 10
            self.label = 'リンゴ'
        elif item_type == 'banana':
            self.color = YELLOW
            self.points = 15
            self.label = 'バナナ'
        elif item_type == 'watermelon':
            self.color = GREEN
            self.points = 20
            self.label = 'スイカ'
        elif item_type == 'bomb':
            self.color = BLACK
            self.points = -15
            self.label = '爆弾'
    
    def fall(self):
        """落下処理"""
        self.y += self.speed
    
    def draw(self, screen):
        """アイテム描画（円）"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.radius, 2)
    
    def is_caught(self, player):
        """衝突判定（円と矩形）"""
        # プレイヤーの矩形
        player_rect = player.get_rect()
        
        # 円の中心がプレイヤーの矩形内にあるか
        if (player_rect.left <= self.x <= player_rect.right and
            player_rect.top <= self.y <= player_rect.bottom):
            return True
        
        return False
    
    def is_off_screen(self):
        """画面外判定"""
        return self.y > HEIGHT + self.radius


def draw_text(screen, text, size, x, y, color=BLACK):
    """テキスト描画のヘルパー関数"""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def main():
    """メインゲームループ"""
    clock = pygame.time.Clock()
    
    # ゲーム変数
    player = Player()
    items = []
    score = 0
    time_left = GAME_TIME
    frame_count = 0
    spawn_timer = 0
    game_over = False
    
    # フォント
    font_large = pygame.font.Font(None, 48)
    font_medium = pygame.font.Font(None, 36)
    
    running = True
    while running:
        clock.tick(FPS)
        
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if not game_over:
            # キー入力
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move("LEFT")
            if keys[pygame.K_RIGHT]:
                player.move("RIGHT")
            
            # アイテム生成
            spawn_timer += 1
            if spawn_timer >= ITEM_SPAWN_INTERVAL:
                spawn_timer = 0
                if len(items) < 3:  # 最大3個まで同時に存在
                    # 70%の確率で良いアイテム、30%で爆弾
                    if random.random() < 0.7:
                        item_type = random.choice(['apple', 'banana', 'watermelon'])
                    else:
                        item_type = 'bomb'
                    items.append(Item(item_type))
            
            # アイテム更新
            for item in items[:]:
                item.fall()
                
                # 衝突判定
                if item.is_caught(player):
                    score += item.points
                    items.remove(item)
                # 画面外判定
                elif item.is_off_screen():
                    items.remove(item)
            
            # タイマー（60FPS = 1秒）
            frame_count += 1
            if frame_count >= FPS:
                frame_count = 0
                time_left -= 1
                if time_left <= 0:
                    game_over = True
        
        # 描画
        screen.fill(GRAY)
        
        # プレイヤー描画
        player.draw(screen)
        
        # アイテム描画
        for item in items:
            item.draw(screen)
        
        # スコア表示
        draw_text(screen, f"Score: {score}", 36, 10, 10)
        
        # タイマー表示
        draw_text(screen, f"Time: {time_left}", 36, WIDTH - 150, 10)
        
        # ゲームオーバー表示
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
            score_text = font_medium.render(f"Final Score: {score}", True, BLACK)
            score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
            screen.blit(score_text, score_rect)
            
            # リスタート案内
            restart_text = font_medium.render("Press ESC to exit", True, BLACK)
            restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 70))
            screen.blit(restart_text, restart_rect)
            
            # ESCキーで終了
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
