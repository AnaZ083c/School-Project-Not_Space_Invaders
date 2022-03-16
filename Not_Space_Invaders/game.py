from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import Enemy, Enemies
from Stars_classes import Star
from functions import *
from Scene import *
from Label import Label
import constants_and_globals as cag

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
fuel_fire = Sprite(sprite_sheet, 3, (4, 0), False)
dash = Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 5), False)

explosion_sprites = Sprite(sprite_sheet, 3, (5, FRAME_OFFSET), False)

# bullet sprites
bullet_sprites = Sprite(sprite_sheet, 3, (3, FRAME_OFFSET * 4), False)
en_bullet_sprites = Sprite(sprite_sheet, 3, (4, FRAME_OFFSET * 4), False)
purple_bullet = Sprite(sprite_sheet, 3, (5, 4 * FRAME_OFFSET), False)
blue_bullet = Sprite(sprite_sheet, 2, (6, 5 * FRAME_OFFSET), False)
yellow_bullet = Sprite(sprite_sheet, 3, (7, 4 * FRAME_OFFSET), False)

player_boss_sprites = Sprite(sprite_sheet, 3, (3, 0), False)  # a special boss

# pickup sprites
heal_pickup = Sprite(sprite_sheet, 1, (6, 0))
yellow_pickup = Sprite(sprite_sheet, 1, (6, FRAME_OFFSET))
green_pickup = Sprite(sprite_sheet, 1, (6, 2 * FRAME_OFFSET))
blue_pickup = Sprite(sprite_sheet, 1, (6, 3 * FRAME_OFFSET))
purple_pickup = Sprite(sprite_sheet, 1, (6, 4 * FRAME_OFFSET))

# enemy sprites
generic_enemy_sprites = Sprite(sprite_sheet, 1, (0, FRAME_OFFSET * 2))
octopus_enemy_sprites = Sprite(sprite_sheet, 2, (7, 0), False)
robot_enemy_sprites = Sprite(sprite_sheet, 2, (7, FRAME_OFFSET * 2), False)
enemies_list.append(generic_enemy_sprites)
enemies_list.append(octopus_enemy_sprites)
enemies_list.append(robot_enemy_sprites)

# boss sprites
angry_alien_boss = Sprite(sprite_sheet, 1, (1, FRAME_OFFSET * 2), False, BOSS_IMAGE_SCALE)
eye_boss = Sprite(sprite_sheet, 5, (0, FRAME_OFFSET * 3), False, BOSS_IMAGE_SCALE)
octopus_boss = Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 3), False, BOSS_IMAGE_SCALE)
robot_boss = Sprite(sprite_sheet, 4, (2, FRAME_OFFSET * 3), False, BOSS_IMAGE_SCALE)
boss_bar = Sprite(sprite_sheet, 6, (1, FRAME_OFFSET * 7), True, BOSS_IMAGE_SCALE)


# health sprites
helth_sprite = Sprite(sprite_sheet, 1, (2, FRAME_OFFSET * 2), True, 0.2)
# helth_sprite.scale = ()
helth_img_size = FRAME_OFFSET * helth_sprite.scale

# death sprite
deth_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 3), True, 2.5)
deth_img_size = FRAME_OFFSET * deth_sprite.scale

# win
win_sprite = Sprite(sprite_sheet, 1, (5, 0), True, 2.5)
win_img_size = FRAME_OFFSET * win_sprite.scale

octoboss_animation = Animation(octopus_boss, 300)

sprites = {
    "heart": helth_sprite,
    "player1": player1_sprites,
    "player2": player2_sprites,
    "player_bullet": bullet_sprites,
    "enemies": enemies_list,
    "enemy_bullet": en_bullet_sprites,
    "death": deth_sprite,
    "win": win_sprite,
    "first-boss": angry_alien_boss,
    "second-boss": octopus_boss,
    "second-boss-animation": octoboss_animation,
    "third-boss": robot_boss,
    "fourth-boss": eye_boss,
    "final-boss": player_boss_sprites,
    "fuel-fire": fuel_fire,
    "dash": dash,
    "explosion": explosion_sprites,
    "purple-bullet": purple_bullet,
    "blue-bullet": blue_bullet,
    "yellow-bullet": yellow_bullet,
    "heal-pickup": heal_pickup,
    "yellow-pickup": yellow_pickup,
    "green-pickup": green_pickup,
    "blue-pickup": blue_pickup,
    "purple-pickup": purple_pickup,
    "boss-bar": boss_bar,
}


def get_sound_state(setting_file: str) -> int:
    # Read the file
    with open(setting_file, 'r') as file:
        current_state = file.read()

    return int(current_state)


def toggle_sound_state(setting_file: str, new_state: int) -> None:
    # Read the file
    with open(setting_file, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(str(cag.sound_state), str(new_state))

    # Write the file out again
    with open(setting_file, 'w') as file:
        file.write(filedata)

    cag.sound_state = new_state


def run_game(starting_scene):
    pygame.mixer.pre_init(44100, -16, 2, 1024)
    pygame.mixer.init(44100, -16, 2, 1024)
    pygame.mixer.set_num_channels(128)
    # pygame.mixer.music.load(THEME)
    # pygame.mixer.music.set_volume(0.15)

    # if cag.sound_state:
    # pygame.mixer.music.play(-1)

    active_scene = starting_scene

    # cag.sound_state = get_sound_state(SETTINGS)

    while active_scene is not None:
        window.clock.tick(FPS)

        pressed_keys = pygame.key.get_pressed()

        # if not cag.sound_state:
        #     pygame.mixer.music.pause()
        # else:
        #     pygame.mixer.music.unpause()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                # if event.key == pygame.K_F1:  # toggle sound 0/1
                #     toggle_sound_state(SETTINGS, int(not cag.sound_state))
                #     # print(cag.sound_state)
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


run_game(TitleScene(sprites))
pygame.quit()
exit(0)
# quit()
