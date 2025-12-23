import pygame

import sys

from rocket import Rocket

from settings import Settings

from bullet import Bullet

from alien import Alien

from random import randint

class Roket_game:
    '''管理火箭游戏的类'''
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Roket Game")
        self.bg_color = Settings().bg_color
        self.ckock = pygame.time.Clock()
        self.rocket = Rocket(self)
        self.alien = Alien(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._creat_fleet()
        
    def run_game(self):
        '''开始游戏循环'''
        while True:
            self.rocket.update()
            self._event_check()
            self._update_bullets()
            self._update_aliens()
            self._screen_update()
            self.ckock.tick(60)

    def _update_aliens(self):
        '''更新外星人信息'''
        self.aliens.update()
        self._check_edge()

    def _check_edge(self):
        '''检查外星人是否在边缘'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        '''改变位置及方向'''
        self.settings.fleet_direction *= -1
        for alien in self.aliens:
            alien.rect.x -= self.settings.alien_right_speed

    def _creat_fleet(self):
        '''创建外形舰队'''
        for I in range(self.settings.alien_num):
            x_position = randint(self.screen_rect.width - 5 * self.alien.rect.width, self.screen_rect.width - 2 * self.alien.rect.width)
            y_position = randint(self.alien.rect.height, self.screen_rect.height - self.alien.rect.height)
            self._creat_alien(x_position,y_position)


    def _creat_alien(self,x_position,y_position):
        '''创建一个外星人'''
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _event_check(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet() 
                elif event.key == pygame.K_q:
                    sys.exit()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False

    def _update_bullets(self):
        '''更新子弹的位置，并删除已消失的子弹'''
        # 每次循环都更新子弹的位置
        self.bullets.update()
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
        if not self.aliens:
            self.bullets.empty()
            self._creat_fleet()
        

    def _fire_bullet(self):
        '''开火'''
        if len(self.bullets) < self.settings.bullet_allowance:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _screen_update(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    rg = Roket_game()
    rg.run_game()

