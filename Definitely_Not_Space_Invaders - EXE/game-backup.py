from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import Enemy, Enemies
from constants_and_globals import *
from Stars_classes import Star
from functions import *
from Scene import *

import random
import pygame


pygame.init()
# window init
window = Window()
window.init_window()

""" 
    Load Assets 
"""
enemies_list = []

sprite_sheet = SpriteSheet(SPRITE_SHEET)

# player sprites
player1_sprites = Sprite(sprite_sheet)
player2_sprites = Sprite(sprite_sheet, 3, (0, FRAME_OFFSET), True)

# bullet sprites
bullet_sprites = Sprite(sprite_sheet, 3, (3, FRAME_OFFSET * 4), False)
en_bullet_sprites = Sprite(sprite_sheet, 3, (4, FRAME_OFFSET * 4), False)

player_boss_sprites = Sprite(sprite_sheet, 3, (3, 0), False)  # a special boss

# enemy sprites
generic_enemy_sprites = Sprite(sprite_sheet, 1, (0, FRAME_OFFSET * 2))
enemies_list.append(generic_enemy_sprites)

# boss sprites
angry_alien_boss = Sprite(sprite_sheet, 1, (1, FRAME_OFFSET * 2))
eye_boss = Sprite(sprite_sheet, 5, (0, FRAME_OFFSET * 3), False)

# boss and or enemy
octopus_boss = Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 3), False)
enemies_list.append(octopus_boss)

robot_boss = Sprite(sprite_sheet, 4, (2, FRAME_OFFSET * 3), False)

# health sprites
helth_sprite = Sprite(sprite_sheet, 1, (2, FRAME_OFFSET * 2), True, 0.2)
# helth_sprite.scale = ()
helth_img_size = FRAME_OFFSET * helth_sprite.scale

# death sprite
deth_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 3), True, 2.5)
deth_img_size = FRAME_OFFSET * deth_sprite.scale

# wave sprites
wave1_sprite = Sprite(sprite_sheet, 1, (3, FRAME_OFFSET * 3))
wave2_sprite = Sprite(sprite_sheet, 1, (4, 0))
wave3_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET))

# it's a boss!! :o
its_a_boss = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 2))

# win
win_sprite = Sprite(sprite_sheet, 1, (5, 0), True, 2.5)
win_img_size = FRAME_OFFSET * win_sprite.scale


menu_font_size = int(60)
menu_font = pygame.font.Font(FONT, menu_font_size)
singleplayer_text = menu_font.render('Singleplayer', True, TITANIUM_HWHITE)
singleplayer_text_rect = singleplayer_text.get_rect()
singleplayer_text_rect.center = (WIDTH/2, HEIGHT/2 - 60)

multiplayer_text = menu_font.render('Multiplayer', True, TITANIUM_HWHITE)
multiplayer_text_rect = multiplayer_text.get_rect()
multiplayer_text_rect.center = (WIDTH/2, HEIGHT/2 + multiplayer_text.get_height() - 50)

options_text = menu_font.render('Options', True, TITANIUM_HWHITE)
options_text_rect = options_text.get_rect()
options_text_rect.center = (WIDTH/2, HEIGHT/2 + options_text.get_height()*2 - 40)

exit_text = menu_font.render('Exit', True, TITANIUM_HWHITE)
exit_text_rect = exit_text.get_rect()
exit_text_rect.center = (WIDTH/2, HEIGHT/2 + exit_text.get_height()*3 - 30)

#  # choose controlls menu
description_text = menu_font.render('Choose device', True, TITANIUM_HWHITE)
description_text_rect = description_text.get_rect()
description_text_rect.center = (WIDTH/2, HEIGHT/2 - 200)

sp_controller_text = menu_font.render('Controller', True, TITANIUM_HWHITE)
sp_controller_text_rect = sp_controller_text.get_rect()
sp_controller_text_rect.center = (WIDTH/2, HEIGHT/2 - 60)

sp_keyboard_text = menu_font.render('Keyboard', True, TITANIUM_HWHITE)
sp_keyboard_text_rect = sp_keyboard_text.get_rect()
sp_keyboard_text_rect.center = (WIDTH/2, HEIGHT/2 + multiplayer_text.get_height() - 50)

back_text = menu_font.render('Back', True, TITANIUM_HWHITE)
back_text_rect = back_text.get_rect()
back_text_rect.center = (WIDTH/2, HEIGHT/2 + exit_text.get_height()*3 - 30)

entername_text = menu_font.render('Enter name', True, TITANIUM_HWHITE)
entername_text_rect = entername_text.get_rect()
entername_text_rect.center = (WIDTH/2, HEIGHT/2 - 60)

description_text2 = menu_font.render('Choose your name', True, TITANIUM_HWHITE)
description_text2_rect = description_text2.get_rect()
description_text2_rect.center = (WIDTH/2, HEIGHT/2 - 200)

description_text3 = menu_font.render('Start your controller first', True, TITANIUM_HWHITE)
description_text3_rect = description_text3.get_rect()
description_text3_rect.center = (WIDTH/2, HEIGHT/2 - 200)

# and press A to continue
description_text3_cont = menu_font.render('and press A on your controller to continue', True, TITANIUM_HWHITE)
description_text3_cont_rect = description_text3_cont.get_rect()
description_text3_cont_rect.center = (WIDTH/2, HEIGHT/2 - 140)

controller_init_font = pygame.font.Font(FONT, 80)
isInited_text = controller_init_font.render('O', True, (0, 255, 0))
isInited_text_rect = isInited_text.get_rect()
isInited_text_rect.center = (WIDTH/2, HEIGHT/2 - 10)

notInited_text = controller_init_font.render('X', True, (255, 0, 0))
notInited_text_rect = notInited_text.get_rect()
notInited_text_rect.center = (WIDTH/2, HEIGHT/2 - 10)

texts = [
    # main menu
    (singleplayer_text, singleplayer_text_rect),    # 0
    (multiplayer_text, multiplayer_text_rect),      # 1
    (options_text, options_text_rect),              # 2
    (exit_text, exit_text_rect),                    # 3

    # choose-device menu
    (description_text, description_text_rect),      # 4
    (sp_controller_text, sp_controller_text_rect),  # 5
    (sp_keyboard_text, sp_keyboard_text_rect),      # 6
    (back_text, back_text_rect),                    # 7

    # enter name
    (entername_text, entername_text_rect),          # 8
    (description_text2, description_text2_rect),    # 9

    # init controller
    (description_text3, description_text3_rect),            # 10
    (description_text3_cont, description_text3_cont_rect),  # 11
    (isInited_text, isInited_text_rect),                    # 12
    (notInited_text, notInited_text_rect)                   # 13

    # game scene stuff

]

sprites = {
    "heart": helth_sprite,
    "player1": player1_sprites,
    "player2": player2_sprites,
    "player_bullet": bullet_sprites,
    "enemies": enemies_list,
    "enemy_bullet": en_bullet_sprites,
    "death": deth_sprite,
    "win": win_sprite
}


def run_game(starting_scene):
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.mixer.init(44100, -16, 2, 1024)
    pygame.mixer.set_num_channels(128)
    pygame.mixer.music.load(THEME)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    active_scene = starting_scene

    while active_scene is not None:
        window.clock.tick(FPS)

        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.show(window)

        active_scene = active_scene.next

        pygame.display.flip()


run_game(TitleScene(sprites, texts))
pygame.quit()
quit()
