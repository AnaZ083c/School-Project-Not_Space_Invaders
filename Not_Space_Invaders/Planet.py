from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from constants_and_globals import *

import random
import pygame

class Planet:
    def __init__(self, planet_sprite: Sprite, fall_speed, spawn_cooldown):
        self.planet_sprite = planet_sprite
        self.animation = Animation(self.planet_sprite, 200)
        self.x = random.uniform(0, WIDTH - planet_image_size)
        self.y = random.uniform(-planet_image_size * 10, -planet_image_size)
        self.top_y = self.y
        self.fall_speed = fall_speed

        self.timer = 0
        self.last_spawn_time = pygame.time.get_ticks()
        self.spawn_cooldown = spawn_cooldown

    def fall(self):
        self.y += self.fall_speed
        self.out_of_bounds_handler()

    def out_of_bounds_handler(self):
        current_time = pygame.time.get_ticks()
        if self.y >= HEIGHT:
            if current_time - self.last_spawn_time >= self.spawn_cooldown:
                self.timer += 1
                self.last_spawn_time = current_time
                if self.timer >= self.spawn_cooldown:
                    self.reset_position()
                    self.timer = 0

    def reset_position(self):
            self.x = random.uniform(0, WIDTH - planet_image_size)
            self.y = random.uniform(-planet_image_size * 10, -planet_image_size)

    def show(self, window: Window):
        self.animation.animate(window, self.x, self.y)
