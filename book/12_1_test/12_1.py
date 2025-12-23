import pygame

import sys

from setting import Setting

class Test:
    def __init__(self):
        pygame.init()
        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Test Window")
        self.clock = pygame.time.Clock()
        self.bg_color = self.setting.bg_color
        self.sprite_sheets = pygame.image.load('book/12_1_test/picture/shipsheetparts.PNG')
        self.sprite_rect = pygame.Rect(18, 10, 45, 45)
        self.image = self.sprite_sheets.subsurface(self.sprite_rect)
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.bg_color = self.setting.bg_color

    def run_test(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Update screen
            self.update_screen()
            self.clock.tick(60)

    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()

if __name__ == '__main__':
    test = Test()
    test.run_test()