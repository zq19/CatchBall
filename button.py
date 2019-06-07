import pygame


class Button():

    def __init__(self,location,screen,offset_x,offset_y):

        self.image = pygame.image.load(location)
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        "按钮初始位置"
        self.rect.centerx = self.screen_rect.centerx + offset_x
        self.rect.centery = self.screen_rect.centery + offset_y

    def blitbutton(self,state):
        if state.game_active == False:
            self.screen.blit(self.image,self.rect)
            pygame.mouse.set_visible(True)


