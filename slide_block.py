import pygame
from pygame.sprite import Sprite


class Slide_block(Sprite):

    def __init__(self,screen):
         super(Slide_block).__init__()
         "加载屏幕和滑块"
         self.screen = screen
         self.image = pygame.image.load('.\images\滑块.png')
         "获取屏幕和滑块的尺寸参数"
         self.rect = self.image.get_rect()
         self.screen_rect = self.screen.get_rect()
         "初始化滑块位置"
         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.bottom
         self.flag_right = False
         self.flag_left = False


    def update(self,setting):
        if self.flag_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += setting.slide_speed
        if self.flag_left and self.screen_rect.left<self.rect.left:
            self.rect.centerx -= setting.slide_speed

    def blitblock(self):
        self.screen.blit(self.image,self.rect)
