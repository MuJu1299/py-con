import sys
from time import sleep
import pygame
from settings import Setting
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard
from pathlib import Path
from pygame import mixer

class AlienInvasion:
    #'''管理游戏资源和行为的类'''
    def __init__(self):
        pygame.init()
        pygame.mixer.init(frequency=44100,size=-16,channels=2,buffer=512)
        self.clock = pygame.time.Clock()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_width()
        self.setting.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # 设置背景颜色
        self.bg_color = self.setting.bg_color
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.stats = GameStats(self)
        self.game_active = False
        self.play_button = Button(self)
        self.set_btn = Button(self)
        self.play_button._prep_msg("play")
        self.set_btn._set_msg('set')
        self.path = Path("book\Alien\storage.txt")
        self.sb = Scoreboard(self)



    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监听键盘和鼠标事件
            self._check_events()
            if self.game_active:
                # 更新飞船位置
                self.ship.update()
                # 更新子弹位置
                self._update_bullets()
                # 更新外星人位置
                self._update_alien()

            # 每次循环都会重绘屏幕
            self._update_screen()
            self.clock.tick(60)



    def _check_aliens_bottom(self):
        '''检查是否有外星人到达了底边'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.setting.screen_height:
                self._ship_hit()
                break

    def _ship_hit(self):
        '''响应与外星人的碰撞'''
        if self.setting.ship_limit > 0:
            # 剩余机会减一
            self.setting.ship_limit -= 1

            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # 清空外星人列表及子弹列表
            self.bullets.empty()
            self.aliens.empty()

            # 创建一个新的舰队，并初始化飞船
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(0.5)
        else:
            self._hc_storage()
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _hc_storage(self):
        '''储存最高评分'''
        storage = self.path.read_text()
        lines = storage.splitlines()
        hc_storage = int(lines[0].rstrip())
        if hc_storage < self.stats.hight_score:
            self.path.write_text(str(self.stats.hight_score))

        
    def _check_fleet_edges(self):
        '''有外星人到达边缘时采取相应的措施'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''将整群外星人下移，并改变它们的方向'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _update_alien(self):
        '''更新外星人群中所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()
        # 碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _create_fleet(self):
        '''创建一个外星舰队'''
        # 创建一个外星人，并计算一行可容纳多少个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x,current_y = alien_width,alien_height
        while current_y < (self.setting.screen_height - (3 * alien_height) - self.ship.rect.height):
            while (current_x + alien_width) < (self.setting.screen_width - alien_width):
                self._create_alien(current_x,current_y)
                current_x += alien_width * 2
            current_x = alien_width
            current_y += alien_height * 2

    def _create_alien(self,x_position,y_position):
        '''创建一个外星人并将其放在当前行'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_bullets(self):
        '''更新子弹的位置，并删除已消失的子弹'''
        # 每次循环都更新子弹的位置
        self.bullets.update()
        # 检查是否有子弹击中了外星人
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,False,True)
        # 击中得分
        # collisions 是一个字典
        # 键：子弹对象
        # 值：与该子弹碰撞的外星人列表
        # collisions = {
        #     bullet1: [alien1, alien2],  # 一个子弹击中了两个外星人
        #     bullet2: [alien3]          # 另一个子弹击中了一个外星人
        #     }
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_point*len(aliens)
                self.sb.prep_score()
                self.sb.check_hight_score()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: 
                self.bullets.remove(bullet)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _check_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
        
    def _check_play_button(self,mouse_pos):
        '''单机Play按钮开始新游戏'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        set_btn_clicked = self.set_btn.set_rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()
            self.sb.prep_level()
            self.sb.prep_ships()
        elif set_btn_clicked:
            self._set_difficulty()
        
    def _set_difficulty(self):
        '''切换难度'''
        self.setting.increase_speed()

            
    def _start_game(self):
        '''开始'''
        # self.setting.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.game_active = True 

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()

        # 隐藏光标
        pygame.mouse.set_visible(False)


    def _check_keydown_events(self,event):
        '''响应按下'''
        # 按下K_RIGHT持续向右移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_p:
            self._start_game()
        # 按下K_LEFT键持续向左移动
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按下退出系统并非关闭窗口
        elif event.key == pygame.K_q:
            sys.exit()
        # 按下空格键发射子弹
        elif event.key == pygame.K_SPACE:
            if self.game_active:
                self._fire_bullet()

    def _fire_bullet(self):
        '''创建一颗子弹，并将其加入编组bullets中'''
        if len(self.bullets) < self.setting.bullet_allowance:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            sound_effect = pygame.mixer.Sound("book\Alien\sound\Shooting.mp3")
            sound_effect.play(loops=0)

    def _check_keyup_events(self,event):
        '''响应松开'''
        # 松开K_RIGHT停止移动
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # 松开K_LEFT键停止移动
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        # 每次循环都重绘屏幕
        self.screen.fill(self.setting.bg_color)
        # 在飞船和子弹后面重绘所有子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        if not self.game_active:
            '''非活动显示按钮'''
            self.play_button.draw_button()
            self.set_btn.draw_set_btn()
        self.sb.show_score()
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()



