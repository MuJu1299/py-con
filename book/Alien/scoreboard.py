import pygame.font
class Scoreboard:
    '''显示得分信息的类'''

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.setting
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        # 准备初始的分图像
        self.prep_score()
        # 最高分
        self.prep_hight_score()

    def prep_hight_score(self):
        '''将最高分渲染为图像'''
        hight_score = round(self.stats.hight_score,-1)
        hight_score_str = f"{hight_score:,}"
        self.hight_score_image = self.font.render(hight_score_str,True,self.text_color,self.settings.bg_color)

        # 将最高分放在顶部
        self.hight_score_image_rect = self.hight_score_image.get_rect()
        self.hight_score_image_rect.centerx = self.screen_rect.centerx
        self.hight_score_image_rect.top = 0
        
    def prep_score(self):
        '''将得分渲染为图像'''
        rounded_score = round(self.stats.score,-1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # 在屏幕左上方显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.height - 40

    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.hight_score_image,self.hight_score_image_rect)

    def check_hight_score(self):
        '''诞生最高分'''
        if self.stats.score > self.stats.hight_score:
            self.stats.hight_score = self.stats.score
            self.prep_hight_score()