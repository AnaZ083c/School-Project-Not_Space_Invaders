from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player
from Enemy_classes import Enemy, Enemies
from constants_and_globals import *
from functions import *
from sprites import *
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

# all_sprites = pygame.sprite.Group()

""" sprites.py code """

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

enemies = read_enemies("test0_0.ens")

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
        enemy.update(player1.bullets + player2.bullets, True)

    for enemy in enemies:
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

    # show frame image
    player1.show(window)
    player2.show(window)

    # enemies_objs.show(window)

    for enemy in enemies:
        enemy.show(window)


    # all_sprites.draw(window.screen)
    pygame.display.flip()  # always after drawing everything!!

pygame.quit()  # close pygame
