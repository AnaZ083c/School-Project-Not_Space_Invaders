from Window import Window
from constants_and_globals import *
import pygame


class Label:
    def __init__(self, string, x, y, color, size, font_file, position: str = '', rect_pos=0):
        self.string = string
        self.x = x
        self.y = y
        self.size = size # int(size * scale)
        self.color = color
        self.position = position
        self.rect_pos = rect_pos
        self.font_file = font_file

        self.font = pygame.font.Font(font_file, self.size)
        self.text = self.font.render(string, True, color)
        self.text_rect = self.text.get_rect()

        self.set_position(self.rect_pos)

    def set_position(self, pos):
        if len(self.position):
            if self.position is 'top':
                self.text_rect.top = pos

            elif self.position is 'left':
                self.text_rect.left = pos

            elif self.position is 'bottom':
                self.text_rect.bottom = pos

            elif self.position is 'right':
                self.text_rect.right = pos

            elif self.position is 'topleft':
                self.text_rect.topleft = pos

            elif self.position is 'bottomleft':
                self.text_rect.bottomleft = pos

            elif self.position is 'topright':
                self.text_rect.topright = pos

            elif self.position is 'bottomright':
                self.text_rect.bottomright = pos

            elif self.position is 'midtop':
                self.text_rect.midtop = pos

            elif self.position is 'midleft':
                self.text_rect.midleft = pos

            elif self.position is 'midbottom':
                self.text_rect.midbottom = pos

            elif self.position is 'midright':
                self.text_rect.midright = pos

            elif self.position is 'center':
                self.text_rect.center = pos

    def update(self, new_string, new_color):
        self.string = new_string
        self.color = new_color
        self.text = self.font.render(self.string, True, self.color)
        self.__init__(self.string, self.x, self.y, self.color, self.size, self.font_file, self.position, self.rect_pos)

    def change_size(self, new_size):
        self.size = new_size
        self.__init__(self.string, self.x, self.y, self.color, self.size, self.font_file, self.position, self.rect_pos)

    def change_xy(self, new_xy):
        self.x, self.y = new_xy
        self.rect_pos = (self.x, self.y)
        self.__init__(self.string, self.x, self.y, self.color, self.size, self.font_file, self.position, self.rect_pos)

    def change_x(self, new_x):
        self.x = new_x
        self.rect_pos = (self.x, self.y)
        self.__init__(self.string, self.x, self.y, self.color, self.size, self.font_file, self.position, self.rect_pos)

    def change_y(self, new_y):
        self.y = new_y
        self.rect_pos = (self.x, self.y)
        self.__init__(self.string, self.x, self.y, self.color, self.size, self.font_file, self.position, self.rect_pos)

    def show(self, window: Window):
        if len(self.position):
            window.screen.blit(self.text, self.text_rect)
        else:
            window.screen.blit(self.text, (self.x, self.y))
