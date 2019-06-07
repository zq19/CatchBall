import pygame
from ball import Ball
from slide_block import Slide_block
import functions as f
from settings import Settings
from button import Button
from game_states import States


def run_game():

    "初始化游戏并建立一个屏幕对象"
    pygame.init()
    "设置"
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    "设置图标"
    icon = pygame.image.load('.\images\动态球.gif')
    pygame.display.set_icon(icon)
    "设置游戏名"
    pygame.display.set_caption("catch_ball")
    "背景图片"
    background = pygame.image.load('.\images\\timg.jpg')
    "生成球"
    ball = Ball(screen)
    "生成滑块"
    slide_block = Slide_block(screen)
    "生成按钮"
    button_play = Button(setting.button_list[0],screen,0,0)
    button_replay = Button(setting.button_list[1], screen, 0, 0)
    button_replayyes = Button(setting.button_list[2], screen, -80, 50)
    button_replayno = Button(setting.button_list[3], screen, 80, 50)
    "生成状态"
    state = States()




    while True:
        screen.blit(background, (0, 0))
        f.check_events(slide_block, button_play,button_replayyes, button_replayno,state,setting)
        button_play.blitbutton(state)
        if state.game_active == True:

            ball.update(slide_block,setting)
            ball.blitball()
            slide_block.update(setting)
            slide_block.blitblock()
        f.check_game_over(ball, button_replay, button_replayyes, button_replayno, state)

        pygame.display.update()

if __name__ == '__main__':
    run_game()
