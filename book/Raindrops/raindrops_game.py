import pygame
from settings import Settings
from raindrops import Raindrops
import sys

class RaindropsGame:
    '''管理雨滴游戏的类'''
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Raindrops Game")
        self.bg_color = (135, 206, 250)  # 天空蓝
        self.clock = pygame.time.Clock()
        self.raindrops = Raindrops(self)
        self.RDS = pygame.sprite.Group()

    def _creat_rains(self):
        '''创建雨'''
        for i in range(100):
            self._creat_raindrops()

    def _creat_raindrops(self):
        '''创建新雨滴'''
        new_raindrops = Raindrops(self)
        self.RDS.add(new_raindrops)


    def _update_screen(self):
        '''更新游戏屏幕'''
        self.screen.fill(self.bg_color)
        # 绘制所有雨滴
        self._creat_raindrops()
        for raindrop in self.RDS:
            raindrop.draw_raindrop()
        pygame.display.flip()
        self.clock.tick(60)

    def _check_event(self):
        '''响应事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _update_raindrops(self):
        '''更新所有雨滴的位置'''
        self.RDS.update() 

    def run_game(self):
        '''游戏开始函数'''
        while True:
            '''持续进行函数'''
            self._update_screen()
            self._update_raindrops()
            self._check_event()



if __name__ == "__main__":
    '''创建游戏实例并开始游戏'''
    RD = RaindropsGame()
    RD.run_game()
