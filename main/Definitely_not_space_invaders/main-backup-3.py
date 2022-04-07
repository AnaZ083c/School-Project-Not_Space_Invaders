from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player
from Enemy_classes import Enemy, Enemies
from constants_and_globals import *
from functions import *
import pygame

# init
pygame.init()
pygame.mixer.init()

# window
window = Window()
window.init_window()

pygame.joystick.init()
joysticks = [None, None, None]
for i in range(pygame.joystick.get_count()):
    joysticks[i] = (pygame.joystick.Joystick(i), pygame.joystick.Joystick(i).get_instance_id())
    pygame.joystick.Joystick(i).init()

print(joysticks)

enemies_list = []

# all_sprites = pygame.sprite.Group()

# sprite_sheet_image = pygame.image.load('assets/sprite-sheet-transparent.png').convert_alpha()
sprite_sheet = SpriteSheet(SPRITE_SHEET)

# player sprites
player1_sprites = Sprite(sprite_sheet)
player2_sprites = Sprite(sprite_sheet, 3, (0, FRAME_OFFSET), True)

# bullet sprites
bullet_sprites = Sprite(sprite_sheet, 3, (3, FRAME_OFFSET*4), False)

player_boss_sprites = Sprite(sprite_sheet, 3, (3, 0), False)  # a special boss

# enemy sprites
generic_enemy_sprites = Sprite(sprite_sheet, 1, (0, FRAME_OFFSET * 2))
enemies_list.append(generic_enemy_sprites)

# boss sprites
angry_alien_boss = Sprite(sprite_sheet, 1, (1, FRAME_OFFSET * 2))
eye_boss = Sprite(sprite_sheet, 5, (0, FRAME_OFFSET * 3), False)
octopus_boss = Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 3), False)
robot_boss = Sprite(sprite_sheet, 4, (2, FRAME_OFFSET * 3), False)

# health sprites
helth_sprite = Sprite(sprite_sheet, 1, (2, FRAME_OFFSET * 2))

# death sprite
deth_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 3))

# wave sprites
wave1_sprite = Sprite(sprite_sheet, 1, (3, FRAME_OFFSET * 3))
wave2_sprite = Sprite(sprite_sheet, 1, (4, 0))
wave3_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET))

# it's a boss!! :o
its_a_boss = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 2))

# win
win_sprite = Sprite(sprite_sheet, 1, (5, 0))

# other code
player1_animation = Animation(player1_sprites, 500)
bullet_animation = Animation(bullet_sprites, 80)

player1 = Player(player1_sprites, image_size, HEIGHT-image_size, bullet_sprites, joysticks, 1)
player2 = Player(player2_sprites, image_size+image_size, HEIGHT-image_size, bullet_sprites, joysticks, 0)

# enemies = [
#     [Enemy(generic_enemy_sprites, 0, 80),   Enemy(generic_enemy_sprites, 150, 80),   Enemy(generic_enemy_sprites, 150*2, 80)],
#     [Enemy(generic_enemy_sprites, 0, 80*2), Enemy(generic_enemy_sprites, 150, 80*2), Enemy(generic_enemy_sprites, 150*2, 80*2)],
#     [Enemy(generic_enemy_sprites, 0, 80*3), Enemy(generic_enemy_sprites, 150, 80*3), Enemy(generic_enemy_sprites, 150*2, 80*3)]
#     ]
#
# enemies_objs = Enemies(enemies)

player2.set_controls({
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d,
    "fire": pygame.K_k
})

# enemies = read_enemies("test0_0.ens", enemies_list, 150, 80)
enemies1 = [
    Enemy(generic_enemy_sprites, 0, 80),   Enemy(generic_enemy_sprites, 150, 80),   Enemy(generic_enemy_sprites, 150*2, 80),
    Enemy(generic_enemy_sprites, 0, 80*2), Enemy(generic_enemy_sprites, 150, 80*2), Enemy(generic_enemy_sprites, 150*2, 80*2),
    Enemy(generic_enemy_sprites, 0, 80*3), Enemy(generic_enemy_sprites, 150, 80*3), Enemy(generic_enemy_sprites, 150*2, 80*3)
    ]

enemies = [
    Enemy(generic_enemy_sprites, 0, 100),
    Enemy(generic_enemy_sprites, 0, 100*2),
    Enemy(generic_enemy_sprites, 0, 100*3),
    Enemy(generic_enemy_sprites, 150, 100),
    Enemy(generic_enemy_sprites, 150*2, 100),
    Enemy(generic_enemy_sprites, 150, 100*2)     # health decreases for 2 instead of 1
    ]


# game loop
while window.running:
    # keep loop running at FPS
    window.clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():
        player1.event_handler(event)
        player2.event_handler(event)
        if event.type == pygame.QUIT:  # if X was clicked
            window.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window.running = False

    # update
    keys = pygame.key.get_pressed()  # checking pressed keys
    player1.update(keys)
    player2.update(keys)

    for enemy in enemies:
        enemy.update(player1.bullets + player2.bullets, enemies)

    for enemy in enemies:
        # if enemy.was_hit:
        #     enemy.helth -= 1

        if enemy.helth <= 0:
            enemies.remove(enemy)

    # for ens in enemies:
    #     for enemy in ens:
    #         if enemy.helth <= 0:
    #             ens.remove(enemy)
    #             enemies_objs.update_2d_array(enemies)
    # enemies_objs.update(player1.bullets + player2.bullets)

    # draw/render
    window.screen.fill(BLACKER_RED)
    # generic_enemy_sprites.show_frames(window, (0, 0))

    # show frame image
    player1.show(window)
    player2.show(window)

    # enemies_objs.show(window)

    for enemy in enemies:
        enemy.show(window)


    # all_sprites.draw(window.screen)
    pygame.display.flip()  # always after drawing everything!!

pygame.quit()  # close pygame
