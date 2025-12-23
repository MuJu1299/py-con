from pygame.sprite import Sprite
import pygame
from random import randint

class Raindrops(Sprite):
    '''管理所有雨滴并输出雨滴信息的类'''
    def __init__(self, Rd_game):
        super().__init__()
        self.screen = Rd_game.screen
        self.settings = Rd_game.settings
        self.color = self.settings.RD_color
        # 创建雨滴像素

        self.rect = pygame.Rect(0,0,self.settings.RD_width,self.settings.RD_hight)
        self.rect.x = randint(0, self.settings.screen_width)  # 随机x位置
        self.rect.y = randint(-100, -10)  # 从屏幕上方开始
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''设置雨的移动'''
        self.x += self.settings.speed_x
        self.y += self.settings.speed_y
        self.rect.x = self.x
        self.rect.y = self.y
        if self.rect.top > self.settings.screen_height:
            self.rect.y = randint(-100, -10)
            self.y = float(self.rect.y)
            self.rect.x = randint(0, self.settings.screen_width)
            self.x = float(self.rect.x)
    
    def draw_raindrop(self):
        '''绘制雨滴'''
        pygame.draw.rect(self.screen, self.color, self.rect)
