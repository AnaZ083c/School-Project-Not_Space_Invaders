from constants_and_globals import *
import pygame

class Window:
    running = True

    # def __init__(self, width, height, bg_color):
    #     self.width = width
    #     self.height = height
    #     self.bg_color = bg_color

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.bg_color = BLACK

    def init_window(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Not Space Invaders')
        self.clock = pygame.time.Clock()

        #window.fill(self.bg_color)
        #pygame.display.flip()