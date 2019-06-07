import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):

    def __init__(self,screen):
        super(Ball, self).__init__()
        "初始化球的位置"
        self.screen = screen
        "加载球的图像"
        a = random.randint(1,12)
        self.image = pygame.image.load('.\images\球'+str(a)+'.png')
        "得到球与屏幕的矩形尺寸"
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        "初始球的位置"
        self.rect.centerx = random.uniform(self.rect.centerx,self.screen_rect.centerx)
        self.rect.centery = random.uniform(self.rect.centery,self.screen_rect.centery)

    def update(self,blide_block,setting):
        "更新球的位置"
        self.rect.centerx += setting.ball_speedx
        self.rect.centery += setting.ball_speedy
        "检测球是否碰到了左右边界"
        if self.rect.right >= self.screen_rect.right or\
            self.rect.left <= self.screen_rect.left:
            setting.ball_speedx = -setting.ball_speedx
        "检测球是否碰到了上边界"
        if self.rect.top <= self.screen_rect.top:
            setting.ball_speedy = -setting.ball_speedy
        "检测球是否碰到了滑块"
        if int(self.rect.bottom) == int(blide_block.rect.top) and\
                int(blide_block.rect.centerx-blide_block.rect.width/2)\
                <= int(self.rect.centerx) <= \
                int(blide_block.rect.centerx+blide_block.rect.width/2):
            setting.ball_speedy = -setting.ball_speedy



    def blitball(self):
        self.screen.blit(self.image,self.rect)



