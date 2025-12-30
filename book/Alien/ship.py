import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''管理飞船的类'''
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船外接图像并获取其外接矩形
        self.sprite_sheete = pygame.image.load('book\Alien\images\shipsheetparts.PNG')
        self.sprite_rect = pygame.Rect(18, 10, 45, 45)
        self.image = self.sprite_sheete.subsurface(self.sprite_rect)
        self.rect = self.image.get_rect()
        self.settings = ai_game.setting

        # 每艘飞船都放在屏幕底端的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 设置飞船x属性的浮点数
        self.x = float(self.rect.x)


        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''飞船置中'''
        self.rect.midbottom = self.screen_rect.midbottom
            