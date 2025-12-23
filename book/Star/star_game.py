import pygame
import sys

from star import Star

class Star_game:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Star Game")
        self.bg_color = (200,200,200) 
        self.stars = pygame.sprite.Group()

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监听键盘和鼠标事件
            self._check_events()
            # 每次循环都会重绘屏幕
            self._update_screen()

    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_s:
                    self._create_star()
    
    def _create_star(self):
        '''创建一个星星并将其加入编组'''
        new_star = Star()
        self.stars.add(new_star)

    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

    

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    sg = Star_game()
    sg.run_game()