class Settings:
    '''存储火箭游戏的所有设置的类'''
    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # 火箭设置
        self.rocket_speed = 1.5

        # 子弹设置
        self.bullet_speed = 3.0
        self.bullet_color = (60,60,60)
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_allowance = 5

        # alien
        self.alien_speed = 2
        self.fleet_direction = 1
        self.alien_right_speed = 10
        self.alien_num = 10
