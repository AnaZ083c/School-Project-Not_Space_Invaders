from Window import Window
from functions import *
import pygame


class Star(object):
    def __init__(self, x, y, fall_speed, color, width: float = 1.0, height: float = 20.0):
        self.color = color
        self.radius = 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fall_speed = fall_speed
        self.rect = pygame.Rect(self.x, self.y, 1, 20)
        self.trail = pygame.Rect(self.x, self.y, 1, 20)
        self.trail_color = pygame.Color(self.color[0], self.color[1], self.color[2], 255)

    def draw_static(self, window: Window):
        pygame.draw.rect(window.screen, self.color, pygame.Rect(self.x, self.y, 1, 1))

    def draw(self, window: Window):
        # pygame.draw.circle(window.screen, self.color, (self.x, self.y), self.radius)
        # pygame.draw.rect(window.screen, self.trail_color, pygame.Rect(self.x, self.y, self.width, self.height))
        # pygame.draw.circle(window.screen, self.color, (self.x + self.width / 2, self.y + self.height * 2), self.width/2)
        # pygame.draw.circle(window.screen, self.color, (self.x + self.width/2, self.y + self.height), self.width)
        pygame.draw.rect(window.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def fall(self):
        self.y += self.fall_speed

    def check_if_i_should_reappear_on_top(self):
        if self.y >= HEIGHT:
            self.y = 0
