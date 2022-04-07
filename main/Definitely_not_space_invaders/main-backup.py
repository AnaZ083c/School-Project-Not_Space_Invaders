from Window import Window
from Sprite import SpriteSheet, Sprite
from constants_and_globals import *
import pygame

# init
pygame.init()
pygame.mixer.init()

# window
window = Window()
window.init_window()

# all_sprites = pygame.sprite.Group()

# sprite_sheet_image = pygame.image.load('assets/sprite-sheet-transparent.png').convert_alpha()
sprite_sheet = SpriteSheet(SPRITE_SHEET)

# player sprites
player1_sprites = Sprite(sprite_sheet)
player2_sprites = Sprite(sprite_sheet, 3, (0, FRAME_OFFSET), True)

player_boss_sprites = Sprite(sprite_sheet, 3, (3, 0), False)  # a special boss

# enemy sprites
generic_enemy_sprites = Sprite(sprite_sheet, 1, (0, FRAME_OFFSET * 2))

# boss sprites
angry_alien_boss = Sprite(sprite_sheet, 1, (1, FRAME_OFFSET * 2))
eye_boss = Sprite(sprite_sheet, 5, (0, FRAME_OFFSET * 3), False)
octopus_boss = Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 3), False)
robot_boss = Sprite(sprite_sheet, 4, (2, FRAME_OFFSET * 3), False)

# helth sprites
helth_sprite = Sprite(sprite_sheet, 1, (2, FRAME_OFFSET * 2))

# deth sprite
deth_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 3))

# wave sprites
wave1_sprite = Sprite(sprite_sheet, 1, (3, FRAME_OFFSET * 3))
wave2_sprite = Sprite(sprite_sheet, 1, (4, 0))
wave3_sprite = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET))

# it's a boss!! :o
its_a_boss = Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 2))

# stonks
stonks_sprite = Sprite(sprite_sheet, 1, (5, 0))

# game loop
while window.running:
    # keep loop running at FPS
    window.clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if X was clicked
            window.running = False

    # update
    # all_sprites.update()

    # draw/render
    window.screen.fill(TITANIUM_HWHITE)

    # show frame image
    player1_sprites.show_frames(window)
    player2_sprites.show_frames(window, (0, FRAME_OFFSET / 2))
    player_boss_sprites.show_frames(window, (0, FRAME_OFFSET * 2 / 2))
    generic_enemy_sprites.show_frames(window, (0, FRAME_OFFSET * 3 / 2))
    angry_alien_boss.show_frames(window, (256 / 2, FRAME_OFFSET * 3 / 2))
    eye_boss.show_frames(window, (256 * 2 / 2, FRAME_OFFSET * 3 / 2))
    octopus_boss.show_frames(window, (0, FRAME_OFFSET * 4 / 2))
    robot_boss.show_frames(window, (0, FRAME_OFFSET * 5 / 2))
    helth_sprite.show_frames(window, (0, FRAME_OFFSET * 6 / 2))
    wave1_sprite.show_frames(window, (256 / 2, FRAME_OFFSET * 6 / 2))
    wave2_sprite.show_frames(window, (256 * 2 / 2, FRAME_OFFSET * 6 / 2))
    wave3_sprite.show_frames(window, (256 * 3 / 2, FRAME_OFFSET * 6 / 2))
    its_a_boss.show_frames(window, (256 * 4 / 2, FRAME_OFFSET * 6 / 2))
    deth_sprite.show_frames(window, (256 * 5 / 2, FRAME_OFFSET * 6 / 2))
    stonks_sprite.show_frames(window, (256 * 6 / 2, FRAME_OFFSET * 6 / 2))

    # all_sprites.draw(window.screen)
    pygame.display.flip()  # always after drawing everything!!

pygame.quit()  # close pygame
