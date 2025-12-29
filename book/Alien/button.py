import pygame.font

class Button:
    '''初始化按钮的属性'''
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的rect对象，并使其居中
        # play_button
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        # set_btn
        self.set_rect = pygame.Rect(0,0,self.width,self.height)
        self.set_rect.topright = self.screen_rect.topright


        # # 按钮的标签只需创建一次
        # self._prep_msg(msg)
        # self._set_msg(msg)

    def _set_msg(self,msg):
        '''设置难度选择按钮的文字'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.set_rect.center

    def _prep_msg(self,msg):
        '''将msg渲染为图像，并使其在按钮上居中'''
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制一个用颜色填充的按钮，在绘制文本'''
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

    def draw_set_btn(self):
        self.screen.fill(self.button_color,self.set_rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)