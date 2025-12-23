import pygame
from random import randint
from pygame.sprite import Sprite
    

class Star(Sprite):
    '''管理星星的类'''
    def __init__(self):
        '''初始化星星并设置其起始位置'''
        super().__init__()
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.sprite_sheet = pygame.image.load('book\Star\images\star.png')
        self.sprite_rect = pygame.Rect(300, 300, 50, 50)
        self.image = self.sprite_sheet.subsurface(self.sprite_rect)
        self.rect = self.image.get_rect()
        # 存储星星的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        random_x = randint(self.rect.width, self.screen_rect.width - self.rect.width)
        random_y = randint(0, self.screen_rect.height - self.rect.height)
        self.x = random_x
        self.y = random_y
        self.rect.x = self.x
        self.rect.y = self.y