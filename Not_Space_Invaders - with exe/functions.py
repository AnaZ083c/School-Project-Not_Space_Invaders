from Enemy_classes import Enemy
from Sprite import *
from constants_and_globals import *

import random

"""
    Reading enemies from file .ens
    ------------------------------
    0 -> no enemy
    1, 2, 3 ..., n -> enemy types
    1: generic enemy

    file naming: levelNUM.ens
    boss file: levelNUM_B.ens

    offset: spacing between enemies
"""


def read_enemies(infilename: str, enemy_ids: list, bullet_sprites: Sprite, x_offset: int = 80, y_offset: int = 150, min_max_shoot_cooldown: tuple = (40.0, 100.0)):
    infile = open(infilename, "r")
    rows, cols = (0, 0)
    ch_num = 0
    ids = [[]]
    enemies_list = []

    for line in infile:
        for ch in line:
            if ch != ' ' and ch != '\n':
                ids[rows].append(ch)
                ch_num += 1
            elif ch == '\n':
                ids.append([])
                continue
        rows += 1
    infile.close()

    cols = ch_num//rows

    min_, max_ = min_max_shoot_cooldown

    for i in range(0, cols):
        curr_x_offset = x_offset * i
        for j in range(0, rows):
            curr_y_offset = y_offset * (j+1)
            if ids[j][i] == '0':
                """ TODO: empty sprite """
                continue

            elif ids[j][i] == '1':
                shoot_cooldown = random.randrange(int(min_), int(max_), 5)
                enemy_sprite = Enemy(enemy_ids[0], curr_x_offset, curr_y_offset, bullet_sprites, shoot_cooldown)
                enemies_list.append(enemy_sprite)
            elif ids[j][i] == '2':
                shoot_cooldown = random.randrange(int(min_), int(max_), 5)
                enemy_sprite = Enemy(enemy_ids[1], curr_x_offset, curr_y_offset, bullet_sprites, shoot_cooldown)
                enemies_list.append(enemy_sprite)

    return enemies_list
