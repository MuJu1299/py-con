import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示生成单个外星人的类'''

    def __init__(self, ai_game):
        '''初始化外星人并设置其起始位置'''
        super().__init__()
        self.screen = ai_game.screen
        # 加载外星人图像并设置其rect属性
        self.sprite_sheet = pygame.image.load('book\Alien\images\shipsheetparts.PNG')
        self.sprite_rect = pygame.Rect(18, 50, 50, 50)
        self.image = self.sprite_sheet.subsurface(self.sprite_rect)
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确水平位置
        self.y = float(self.rect.y)
        self.settings = ai_game.settings

    def update(self):
        '''向右移动外星人,输出水平位置'''
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
    
    def check_edges(self):
        '''如果外星人位于屏幕边缘，就返回True'''
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0)