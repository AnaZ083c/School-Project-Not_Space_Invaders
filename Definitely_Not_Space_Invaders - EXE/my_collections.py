from constants_and_globals import *
import Sprite as spr

enemies_list = []
sprite_sheet = spr.SpriteSheet(SPRITE_SHEET)

# player sprites
player1_sprites = spr.Sprite(sprite_sheet)
player2_sprites = spr.Sprite(sprite_sheet, 3, (0, FRAME_OFFSET), True)

# bullet sprites
bullet_sprites = spr.Sprite(sprite_sheet, 3, (3, FRAME_OFFSET*4), False)
en_bullet_sprites = spr.Sprite(sprite_sheet, 3, (4, FRAME_OFFSET*4), False)

player_boss_sprites = spr.Sprite(sprite_sheet, 3, (3, 0), False)  # a special boss

# enemy sprites
generic_enemy_sprites = spr.Sprite(sprite_sheet, 1, (0, FRAME_OFFSET * 2))
enemies_list.append(generic_enemy_sprites)

# boss sprites
angry_alien_boss = spr.Sprite(sprite_sheet, 1, (1, FRAME_OFFSET * 2))
eye_boss = spr.Sprite(sprite_sheet, 5, (0, FRAME_OFFSET * 3), False)

# boss and or enemy
octopus_boss = spr.Sprite(sprite_sheet, 2, (1, FRAME_OFFSET * 3), False)
enemies_list.append(octopus_boss)

robot_boss = spr.Sprite(sprite_sheet, 4, (2, FRAME_OFFSET * 3), False)

# health sprites
helth_sprite = spr.Sprite(sprite_sheet, 1, (2, FRAME_OFFSET * 2), True, 0.2)
helth_img_size = FRAME_OFFSET * helth_sprite.scale

# death sprite
deth_sprite = spr.Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 3), True, 2.5)
deth_img_size = FRAME_OFFSET * deth_sprite.scale

# wave sprites
wave1_sprite = spr.Sprite(sprite_sheet, 1, (3, FRAME_OFFSET * 3))
wave2_sprite = spr.Sprite(sprite_sheet, 1, (4, 0))
wave3_sprite = spr.Sprite(sprite_sheet, 1, (4, FRAME_OFFSET))

# it's a boss!! :o
its_a_boss = spr.Sprite(sprite_sheet, 1, (4, FRAME_OFFSET * 2))

# win
win_sprite = spr.Sprite(sprite_sheet, 1, (5, 0), True, 2.5)
win_img_size = FRAME_OFFSET * win_sprite.scale

