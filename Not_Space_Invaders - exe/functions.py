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


def read_enemies(infilename: str, enemy_ids: list, boom: Sprite, bullets: list, x_offset: int = 80, y_offset: int = 150, min_max_shoot_cooldown: tuple = (40.0, 100.0)):
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
                continue

            elif ids[j][i] == '1':
                shoot_cooldown = random.randrange(int(min_), int(max_), 5)
                enemy_sprite = Enemy(boom, enemy_ids[0], curr_x_offset, curr_y_offset, bullets[0], shoot_cooldown, 3, 1, 3)
                enemies_list.append(enemy_sprite)
            elif ids[j][i] == '2':
                shoot_cooldown = random.randrange(int(min_), int(max_), 5)
                enemy_sprite = Enemy(boom, enemy_ids[1], curr_x_offset, curr_y_offset, bullets[1], shoot_cooldown, 5, 2, 5)
                enemies_list.append(enemy_sprite)
            elif ids[j][i] == '3':
                shoot_cooldown = random.randrange(int(min_), int(max_), 5)
                enemy_sprite = Enemy(boom, enemy_ids[2], curr_x_offset, curr_y_offset, bullets[2], shoot_cooldown, 7, 3, 7)
                enemies_list.append(enemy_sprite)

    return enemies_list

def save_points(pts_path, players: list):
    pts_file = open(pts_path, "a")
    for player, player_name in players:
        # print(f"{str(player_name)} {player.points}")
        pts_file.write(f"{str(player_name).ljust(7)} ..... {player.points}\n")

    pts_file.close()

def create_random_levels():
    max_points = 0
    for lvl in range(1, 6):
        for wv in range(1, 4):
            file = open(LEVELS+"level"+str(lvl)+"_"+str(wv)+".ens", "w")

            for i in range(4):
                for j in range(12):
                    enemy_id = random.randint(0, 3)
                    if lvl == 1:
                        enemy_id = random.randint(0, 1)
                    elif lvl == 2:
                        enemy_id = random.randint(0, 2)
                    elif lvl >= 3:
                        enemy_id = random.randint(0, 3)
                    if enemy_id == 1:
                        max_points += 3
                    elif enemy_id == 2:
                        max_points += 5
                    elif enemy_id == 3:
                        max_points += 7
                    file.write(str(enemy_id)+" ")
                file.write("\n")

            file.close()
    return max_points

def get_points_percent(max_points, current_points):
    return (current_points * 100) / max_points

