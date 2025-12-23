import pygame

class Rocket:
    '''管理火箭的类'''
    def __init__(self,rg_game):
        self.screen = rg_game.screen
        self.screen_rect = rg_game.screen.get_rect()
        
        # 加载火箭图像并获取其外接矩形
        self.sprite_sheete = pygame.image.load('book\Rocket\images\shipsheetparts.PNG')
        self.sprite_rect = pygame.Rect(18, 10, 45, 45)
        self.image = self.sprite_sheete.subsurface(self.sprite_rect)
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.settings = rg_game.settings
        # 移动标志
        self.moving_up = False
        self.moving_down = False
        # 设置火箭y属性的浮点数
        self.y = float(self.rect.y)

    def update(self):
        '''根据移动标志调整火箭的位置'''
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        self.rect.y = self.y

    def blitme(self):
        '''在指定位置绘制火箭'''
        self.screen.blit(self.image,self.rect)