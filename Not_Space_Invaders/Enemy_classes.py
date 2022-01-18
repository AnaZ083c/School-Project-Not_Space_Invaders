from Sprite import Sprite, Animation
import Player_classes as pc
from constants_and_globals import *
from Window import Window
import pygame


class Enemy:
    def __init__(self, enemy_sprites: Sprite, x, y, bullet_sprites: Sprite, shoot_cooldown: float = 40.0, worth: int = 3):  # keyboard_controls = [ up, down, left, right ]
        self.enemy_sprites = enemy_sprites
        self.helth = 3
        self.was_hit = False
        self.worth = worth
        self.hit_by_player_num = 0

        self.x = x
        self.y = y

        self.en_bullet_x = self.x
        self.en_bullet_y = self.y
        self.en_bullets = []
        self.en_bullet_shot = True

        self.bullet_sprites = bullet_sprites
        self.en_bullet_x = self.x
        self.en_bullet_y = self.y
        self.en_bullet = pc.Bullet(bullet_sprites, self, self.en_bullet_x, self.en_bullet_y)

        self.move_speed = 2
        self.bullet_speed = 2.5
        self.is_moving = False

        self.last_update = pygame.time.get_ticks()
        self.shoot_cooldown = shoot_cooldown
        self.timer = 0
        self.direction = 1

        self.sfx = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

    # moving and stuff
    def update(self, bullet_list, enemies, is_group: bool = False):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
            self.timer += 1
            self.last_update = current_time
            if self.timer >= self.shoot_cooldown:
                # play shoot sfx
                self.sfx.play()
                # shoot
                self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y))
                self.timer = 0

        self.x += (self.move_speed * self.direction)

        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler(enemies, is_group)

    # change moving speed
    def set_move_speed(self, new_move_speed):
        self.move_speed = new_move_speed

    def out_of_bounds_handler(self, enemies: list, is_group: bool):
        if not is_group:
            if self.x + image_size > WIDTH:
                self.x = WIDTH - image_size
                self.y += self.enemy_sprites.img_size/4
                self.direction = -1
            if self.x < 0:
                self.x = 0
                self.y += self.enemy_sprites.img_size/4
                self.direction = 1
            if self.y + image_size >= HEIGHT:
                self.y = HEIGHT - image_size
            if self.y < 0:
                self.y = 0
        else:
            self.out_of_bounds_group_handler(enemies)

    def out_of_bounds_group_handler(self, enemies: list):
        if len(enemies) > 0:
            if enemies[-1].x + image_size > WIDTH:
                enemies[-1].x = WIDTH - image_size
                self.change_enemies_group_directions(enemies, -1)
            if enemies[0].x < 0:
                enemies[0].x = 0
                self.change_enemies_group_directions(enemies, 1)

    def change_enemies_group_directions(self, enemies: list, new_direction):
        for enemy in enemies:
            enemy.y += enemy.enemy_sprites.img_size/4
            enemy.direction = new_direction

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + 50) and (self.y - 50 <= bullet.y <= self.y + 50):
                bullet.hit = True
                self.was_hit = True
                self.helth -= 1
                self.hit_by_player_num = bullet.owner.player_num
                print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def show(self, window: Window):
        for bullet in self.en_bullets:
            bullet.collision_handler()
            bullet.show(window, self.bullet_speed, False)

            print(bullet.y >= HEIGHT)
            if bullet.y >= HEIGHT-100 or bullet.hit:
                self.en_bullets.remove(bullet)
        window.screen.blit(self.enemy_sprites.frames[0], (self.x, self.y))


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Enemies:
    def __init__(self, enemies_2d_array):
        self.enemies_2d_array = enemies_2d_array
        # self.enemies = []

    def update(self, bullet_list):
        self.bullet_collision_handler(bullet_list)
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                enemy.update(bullet_list, True)
        self.out_of_bounds_handler()

    def out_of_bounds_handler(self):
        for enemies in self.enemies_2d_array:
            if len(enemies) > 0:
                if enemies[-1].x + image_size > WIDTH:
                    enemies[-1].x = WIDTH - image_size
                    self.change_all_directions(-1)
                if enemies[0].x < 0:
                    enemies[0].x = 0
                    self.change_all_directions(1)
                # if self.enemies_2d_array[-1][0].y + image_size >= HEIGHT:
                #     self.enemies_2d_array[-1][0].y = HEIGHT - image_size
                # if self.enemies_2d_array[0][0].y < 0:
                #     self.enemies_2d_array[0][0].y = 0

    def change_all_directions(self, new_direction):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                enemy.direction = new_direction

    def helth_check(self):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                print(enemy.helth)
                if enemy.helth <= 0:
                    enemies.remove(enemy)

    def update_2d_array(self, new_2d):
        self.enemies_2d_array = new_2d

    def bullet_collision_handler(self, bullet_list):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                if len(enemies) > 0:
                    enemy.bullet_collision_handler(bullet_list)
                # for bullet in bullet_list:
                #     if (enemy.x - 50 <= bullet.x <= enemy.x + 50) and bullet.y <= enemy.y + 50:
                #         bullet.hit = True
                #         enemy.was_hit = True
                #         # self.helth -= 1
                #         print(enemy.helth)
                #     else:
                #         bullet.hit = False
                #         enemy.was_hit = False

    def show(self, window: Window):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                enemy.show(window)

