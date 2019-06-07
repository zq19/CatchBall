import sys
import pygame
from game_runner import run_game



def check_key_down(event,slide_block,setting):
    "监测键盘键按下"
    if event.key == pygame.K_RIGHT:
        slide_block.flag_right = True
        check_space_down(event, setting)


    elif event.key == pygame.K_LEFT:
        slide_block.flag_left = True
        check_space_down(event, setting)


def check_key_up(event,slide_block,setting):
    "监测键盘键抬起"
    if event.key == pygame.K_RIGHT:
        slide_block.flag_right = False
        check_space_down(event, setting)

    elif event.key == pygame.K_LEFT:
        slide_block.flag_left = False
        check_space_down(event, setting)



def check_events(slide_block,button,button_replayyes,button_replayno,state,setting):
    "检查键盘键及鼠标动作"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, slide_block,setting)
            check_space_down(event,setting)
        elif event.type == pygame.KEYUP:
            check_key_up(event, slide_block,setting)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_paly_button(button,mouse_x,mouse_y,state)
            check_repalyyes_button(button_replayyes, mouse_x, mouse_y, state)
            check_repalyno_button(button_replayno, mouse_x, mouse_y, state)



def check_paly_button(button,mouse_x,mouse_y,state):
    "检查是否按下了play按钮"
    check_botton = button.rect.collidepoint(mouse_x,mouse_y)
    if check_botton and not state.game_active:
        pygame.mouse.set_visible(False)
        state.game_active = True
        pygame.mixer.music.load(".\images\water.mp3")
        pygame.mixer.music.play(100,0)

def check_game_over(ball,button_replay,button_replayyes,button_replayno,state):
    "检查球是否出界"
    if ball.rect.centery >= ball.screen_rect.height:
        state.game_active = False
        button_replay.blitbutton(state)
        button_replayyes.blitbutton(state)
        button_replayno.blitbutton(state)

def check_repalyyes_button(button_replayyes,mouse_x,mouse_y,state):
    "检查是否点击了yes按钮"
    check_botton = button_replayyes.rect.collidepoint(mouse_x,mouse_y)
    if check_botton and not state.game_active:
        return run_game()

def check_repalyno_button(button_replayno,mouse_x,mouse_y,state):
    "检查是点击了no按钮"
    check_botton = button_replayno.rect.collidepoint(mouse_x,mouse_y)
    if check_botton and not state.game_active:
        sys.exit()

def check_space_down(event,setting):
    "使用setting.count来记录按下空格的次数"
    if event.key == pygame.K_SPACE:
        setting.count += 1
        "使用列表来记录暂停之前的球的速度"
        setting.past_speed.extend([setting.ball_speedx,
                               setting.ball_speedy,setting.slide_speed])
        print(setting.past_speed)

        if int(setting.count%2) == 0:
            "暂停之后球速设置为0"
            pygame.mixer.music.pause()
            setting.ball_speedx = 0
            setting.ball_speedy = 0
            setting.slide_speed = 0
        else:
            pygame.mixer.music.unpause()
            "删除暂停之后为0的三个速度"
            del setting.past_speed[-1]
            del setting.past_speed[-1]
            del setting.past_speed[-1]
            "将最近一次的速度赋值"
            setting.ball_speedx = setting.past_speed[-3]
            setting.ball_speedy = setting.past_speed[-2]
            setting.slide_speed = setting.past_speed[-1]





