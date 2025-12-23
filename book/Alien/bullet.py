import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船所发射子弹的类'''

    def __init__(self,aigame):
        '''在飞船当前的位置创建一个发射子弹的类'''
        super().__init__()
        self.screen = aigame.screen
        self.setting = aigame.setting
        self.color = self.setting.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，在设置正确的位置
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,
                                self.setting.bullet_height)
        self.rect.midtop = aigame.ship.rect.midtop
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动子弹'''
        # 更新表示子弹位置的小数值
        self.y -= self.setting.bullet_speed
        # 更新表示子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)