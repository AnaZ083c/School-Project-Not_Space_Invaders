from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import Enemy, Enemies
from constants_and_globals import *
from Stars_classes import Star
from functions import *
from Label import Label

import random
import pygame

# init
pygame.init()

# window
window = Window()
window.init_window()

pygame.joystick.init()
joysticks = [None, None]
for i in range(pygame.joystick.get_count()):
    joysticks[i] = (pygame.joystick.Joystick(i), pygame.joystick.Joystick(i).get_instance_id())
    pygame.joystick.Joystick(i).init()

print(joysticks)

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

""""""""""""""""""""""""""""""""""""""""""""""""" ACTUAL GAME CODE """""""""""""""""""""""""""""""""""""""""""""""""
player1_animation = Animation(player1_sprites, 500)
bullet_animation = Animation(bullet_sprites, 80)

octoboss_animation = Animation(octopus_boss, 300)

player1 = Player(helth_sprite, player1_sprites, image_size, HEIGHT-image_size, bullet_sprites, joysticks, 1)
player2 = Player(helth_sprite, player2_sprites, image_size+image_size, HEIGHT-image_size, bullet_sprites, joysticks, 2)

player2.set_controls({
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d,
    "fire": pygame.K_k
})

enemies = read_enemies("test0_0.ens", enemies_list, en_bullet_sprites, 150, 80)
print(enemies)

# font = pygame.font.SysFont("Not_space_invaders_font", 40)
p1_title_label = Label('Player 1', helth_img_size - 40, 15, TITANIUM_HWHITE, 40, FONT)
p2_title_label = Label('Player 2', WIDTH - helth_img_size - 110, 15, TITANIUM_HWHITE, 40, FONT)

p1_points_label = Label(str(player1.points), helth_img_size, 80, TITANIUM_HWHITE, 40, FONT, 'topleft', (helth_img_size, 80))
p2_points_label = Label("{p2}".format(p2=player2.points), WIDTH - helth_img_size, 80, TITANIUM_HWHITE, 40, FONT, 'topright', (WIDTH - helth_img_size, 80))


stars = []
fall_speed = 15
for i in range(50):
    x = random.randint(1, WIDTH - 1)
    y = random.randint(1, HEIGHT - 1)
    fall_speed = random.randint(1, 16)
    width = 1
    height = width + fall_speed * 2

    star = Star(x, y, fall_speed, TITANIUM_HWHITE, width, height)
    stars.append(star)

""""""""""""""""""""""""""""""""""""""""""" GAME LOOP """""""""""""""""""""""""""""""""""""""""""
while window.running:
    window.clock.tick(FPS)  # keep loop running at FPS

    """"""""""""""""""""""""""""""""""""" process input (events) """""""""""""""""""""""""""""""""""""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # if X was clicked
            window.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.running = False

    """"""""""""""""""""""""""""""""""""""""""""" update """""""""""""""""""""""""""""""""""""""""""""
    keys = pygame.key.get_pressed()  # checking pressed keys



    """"""""""""""""""""""""""""""""""""""" draw/render """""""""""""""""""""""""""""""""""""""
    window.screen.fill(BLACK)
    for star in stars:
        star.draw(window)
        star.fall()
        star.check_if_i_should_reappear_on_top()

    # show frame image
    window.screen.blit(boss_bar.frames[5], (BOSS_IMAGE_SCALE + WIDTH/2.25, BOSS_IMAGE_SCALE))

    """""""""""""""""""""""""""""""""""""""" flip display """""""""""""""""""""""""""""""""""""""""
    pygame.display.flip()  # always after drawing everything!!

""""""""""""""""""""""""""" quit """""""""""""""""""""""""""
pygame.quit()  # close pygame
quit()

