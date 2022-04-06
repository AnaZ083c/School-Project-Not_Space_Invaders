from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import *
from constants_and_globals import *
from Stars_classes import Star
from functions import *
from Label import Label
from Pickup import Pickup

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
planets_sprite_sheet = SpriteSheet(PLANETS_SPRITE_SHEET)

icon = pygame.image.load(ICON)
pygame.display.set_icon(icon)

# player sprites
player1_sprites = Sprite(sprite_sheet)
player2_sprites = Sprite(sprite_sheet, 3, (0, FRAME_OFFSET), True)
fuel_fire = Sprite(sprite_sheet, 3, (4, 0), False)
dash_left_right = Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 5), False)
dash_up_down = Sprite(sprite_sheet, 2, (9, 0), False)

explosion_sprites = Sprite(sprite_sheet, 3, (5, FRAME_OFFSET), False)

# bullet sprites
bullet_sprites = Sprite(sprite_sheet, 3, (3, FRAME_OFFSET * 4), False)
player_blue_bullet = Sprite(sprite_sheet, 2, (6, 5 * FRAME_OFFSET), False)
player_green_bullet = Sprite(sprite_sheet, 3, (8, 4 * FRAME_OFFSET), False)
player_purple_bullet = Sprite(sprite_sheet, 3, (5, 4 * FRAME_OFFSET), False)
player_yellow_bullet = Sprite(sprite_sheet, 3, (9, 2 * FRAME_OFFSET), False)

en_bullet_sprites = Sprite(sprite_sheet, 3, (4, FRAME_OFFSET * 4), False)
enemy_blue_bullet = Sprite(sprite_sheet, 2, (9, FRAME_OFFSET * 5), False)
enemy_purple_bullet = Sprite(sprite_sheet, 3, (8, FRAME_OFFSET), False)
enemy_yellow_bullet = Sprite(sprite_sheet, 3, (7, 4 * FRAME_OFFSET), False)

player_boss_sprites = Sprite(sprite_sheet, 3, (3, 0), False)  # a special boss

# pickup sprites
heal_pickup = Sprite(sprite_sheet, 8, (0, 8 * FRAME_OFFSET))
red_pickup = Sprite(sprite_sheet, 1, (8, 0))
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
boos_explosion = Sprite(sprite_sheet, 3, (5, FRAME_OFFSET), False, BOSS_IMAGE_SCALE)

# health sprites
helth_sprite = Sprite(sprite_sheet, 1, (2, FRAME_OFFSET * 2), True, 0.2)
dead_heart_sprite = Sprite(sprite_sheet, 1, (3, 3 * FRAME_OFFSET), True, 0.2)
# helth_sprite.scale = ()
helth_img_size = FRAME_OFFSET * helth_sprite.scale

# death sprite
deth_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 3), True, 2.5)
deth_img_size = FRAME_OFFSET * deth_sprite.scale

# win
win_sprite = Sprite(sprite_sheet, 1, (5, 0), True, 2.5)
win_img_size = FRAME_OFFSET * win_sprite.scale

# PLANETS
planet1_sprites = Sprite(planets_sprite_sheet, 5, (0, 0), True, PLANET_SCALE * 0.8)
planet2_sprites = Sprite(planets_sprite_sheet, 5, (0, FRAME_OFFSET), True, PLANET_SCALE * 1.5)
planet3_sprites = Sprite(planets_sprite_sheet, 5, (0, 2 * FRAME_OFFSET), True, PLANET_SCALE)

octoboss_animation = Animation(octopus_boss, 300)
heal_animation = Animation(heal_pickup, 150)
boom_animation = Animation(explosion_sprites, 200)
boss_boom_animation = Animation(boos_explosion, 250)
octopuss_enemy_animation = Animation(octopus_enemy_sprites, 400)
robot_enemy_animation = Animation(robot_enemy_sprites, 400)
fire_animation = Animation(fuel_fire, 100)
red_bullet_animation = Animation(bullet_sprites, 200)
green_bullet_animation = Animation(player_green_bullet, 200)
yellow_bullet_animation = Animation(player_yellow_bullet, 200)
purple_bullet_animation = Animation(player_purple_bullet, 200)
blue_bullet_animation = Animation(player_blue_bullet, 200)
player1_animations = Animation(player1_sprites, 250)
player2_animations = Animation(player2_sprites, 250)
player_boss_animations = Animation(player_boss_sprites, 250)
eye_boss_animations = Animation(eye_boss, 300)
robot_boss_animations = Animation(robot_boss, 300)
boss_bar_animations = Animation(boss_bar, 300)
dash_left_right_animations = Animation(dash_left_right, 350)
dash_up_down_animations = Animation(dash_up_down, 350)


planet1_animation = Animation(planet1_sprites, 200)
planet2_animation = Animation(planet2_sprites, 250)
planet3_animation = Animation(planet3_sprites, 250)


pickup = Pickup(green_pickup)
planet = pygame.image.load(PLANET)


bosses = [
    FirstBoss(explosion_sprites, boss_bar, angry_alien_boss, WIDTH / 2, HEIGHT / 4, enemy_purple_bullet, 20.0),
    SecondBoss(explosion_sprites, boss_bar, octopus_boss, WIDTH / 2, HEIGHT / 4, enemy_purple_bullet, 20.0),
    ThirdBoss(explosion_sprites, boss_bar, robot_boss, WIDTH / 2, HEIGHT / 4, enemy_blue_bullet, 15.0),
    FourthBoss(explosion_sprites, boss_bar, eye_boss, WIDTH / 2, HEIGHT / 4, enemy_yellow_bullet, 10.0),
    FinalBoss(explosion_sprites, boss_bar, player_boss_sprites, WIDTH / 2, HEIGHT / 4, enemy_purple_bullet, 5.0),
]

stars = []
fall_speed = 15 * scale
for i in range(100):
    x = random.randint(1, WIDTH - 1)
    y = random.randint(1, HEIGHT - 1)
    star_color = random.randint(0, len(star_colors)-1)
    fall_speed = random.randint(1, 16) * scale
    width = star_sizes[star_color] # 1
    height = (width * scale) + fall_speed * 2

    star = Star(x, y, fall_speed, star_colors[star_color], width, height)
    stars.append(star)

def animate_stars(window: Window):
    global star
    for star in stars:
        star.draw(window)
        star.fall()
        star.check_if_i_should_reappear_on_top()

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

    # for boss in bosses:
    #     boss.update([])

    """"""""""""""""""""""""""""""""""""""" draw/render """""""""""""""""""""""""""""""""""""""
    window.screen.fill(BLACK)
    for star in stars:
        star.draw(window)
        star.fall()
        star.check_if_i_should_reappear_on_top()

    # for boss in bosses:
    #     boss.show(window)

    # show frame image
    animate_stars(window)

    # planet1_animation.animate(window, planet_image_size, (HEIGHT/2) - planet_image_size/2)
    # planet2_animation.animate(window, planet_image_size * 3, (HEIGHT/2) - planet_image_size/2)
    # planet3_animation.animate(window, planet_image_size * 5, (HEIGHT/2) - planet_image_size/2)

    # heal_animation.animate(window, 0, 0)
    # octoboss_animation.animate(window, image_size, 0)
    # boom_animation.animate(window, boss_image_size * 2, 0)
    # boss_boom_animation.animate(window, boss_image_size * 3, 0)
    # octopuss_enemy_animation.animate(window, boss_image_size * 4, 0)
    # robot_enemy_animation.animate(window, boss_image_size * 5, 0)
    # fire_animation.animate(window, boss_image_size * 6, 0)
    # red_bullet_animation.animate(window, boss_image_size * 7, 0)
    #
    # green_bullet_animation.animate(window, 0, boss_image_size)
    # yellow_bullet_animation.animate(window, image_size, boss_image_size)
    # purple_bullet_animation.animate(window, image_size * 2, boss_image_size)
    # blue_bullet_animation.animate(window, image_size * 3, boss_image_size)
    #
    # player1_animations.animate(window, image_size * 4, boss_image_size)
    # player2_animations.animate(window, image_size * 5, boss_image_size)
    # player_boss_animations.animate(window, image_size * 6, boss_image_size)
    # eye_boss_animations.animate(window, image_size * 7, boss_image_size)
    # robot_boss_animations.animate(window, image_size * 9, boss_image_size)
    # boss_bar_animations.animate(window, image_size * 11, boss_image_size)
    # dash_left_right_animations.animate(window, image_size * 13, boss_image_size)
    # dash_up_down_animations.animate(window, image_size * 14, boss_image_size)



    """""""""""""""""""""""""""""""""""""""" flip display """""""""""""""""""""""""""""""""""""""""
    pygame.display.flip()  # always after drawing everything!!

""""""""""""""""""""""""""" quit """""""""""""""""""""""""""
pygame.quit()  # close pygame
quit()

