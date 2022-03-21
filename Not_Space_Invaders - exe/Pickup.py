from Sprite import *
from Window import Window
from constants_and_globals import *
from Player_classes import Player

import random
import pygame


class Pickup:
    def __init__(self, pickup_sprite: Sprite, spawn_cooldown: float = 2.0, fall_speed: float = 1.5, sfx_index: int = 0, name: str = "pickup", bullet_sprite: Sprite = None, dmg_give: int = 0, shoot_cooldown: int = 20):
        self.pickup_sprite = pickup_sprite
        self.name = name
        self.bullet_sprite = bullet_sprite
        self.x = random.uniform(0, WIDTH - image_size)
        self.y = random.uniform(-image_size*10, -image_size)
        self.fall_speed = fall_speed
        self.dir_x = 0
        self.timer = 0
        self.dmg_give = dmg_give
        self.shoot_cooldown = shoot_cooldown

        self.sfx_index = sfx_index
        self.pickup_sfx = pygame.mixer.Sound(pickup_sfxs[self.sfx_index])
        self.pickup = False
        self.out_of_bounds = False

        self.last_spawn_time = pygame.time.get_ticks()
        self.spawn_cooldown = spawn_cooldown

    def reset_position(self):
        self.x = random.uniform(-image_size, WIDTH - image_size)
        self.y = random.uniform(-image_size*2, -image_size)
        self.pickup = False
        self.out_of_bounds = False

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.pickup or (self.y >= HEIGHT):
            if current_time - self.last_spawn_time >= self.spawn_cooldown:
                self.timer += 1
                self.last_spawn_time = current_time
                if self.timer >= self.spawn_cooldown:
                    self.reset_position()
                    self.timer = 0

        self.x += self.dir_x
        self.y += (self.fall_speed * 1)

    def collision_with_player(self, player: Player):
        if (self.x <= player.x <= self.x + IMAGE_SCALE) and (self.y + IMAGE_SCALE <= player.y <= self.y):
            self.pickup_sfx.play()
            self.pickup = True
            self.last_spawn_time = pygame.time.get_ticks()

    def show(self, window: Window):
        if self.y < HEIGHT and not self.pickup:
            window.screen.blit(self.pickup_sprite.frames[0], (self.x, self.y))
