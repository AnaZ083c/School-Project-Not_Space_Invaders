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


class Planets:
    def __init__(self, sprites: list):
        self.sprites = sprites
        self.planets = []

        self.generate()

    def generate(self):
        maxsize = max([sprite.img_size for sprite in self.sprites])

        for sprite in self.sprites:
            # r = random.randint(1, 5)
            a = 0.002
            # b = 0.005
            fall_speed = a * (maxsize * 1.1 - sprite.img_size) # ((a * r/5) + (b * (1 - r/5))) * (maxsize * 1.1 - sprite.img_size)
            spawn_cooldown = random.randint(10, 50)

            self.planets.append(Planet(sprite, fall_speed, spawn_cooldown))

    def animate(self, window: Window):
        for planet in self.planets:
            planet.show(window)
            planet.fall()


