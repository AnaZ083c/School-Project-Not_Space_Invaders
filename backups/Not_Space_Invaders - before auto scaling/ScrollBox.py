from Window import Window
from constants_and_globals import *
import pygame

class ScrollBox:
    def __init__(self, labels: list, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.labels = labels

        self.color = (255, 255, 255)
        self.scroller_color = (176, 176, 176)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.scroller_rect = pygame.Rect(self.x + self.width - 25, self.y + 10, 15, 100)

    def get_first_label(self):
        return self.labels[0]

    def get_last_label(self):
        return self.labels[len(self.labels)-1]

    def handle_event(self, event):
        first_label = self.get_first_label()
        last_label = self.get_last_label()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for label in self.labels:
                    label.change_y(label.y - 30)
                self.scroller_rect.y += 40
            elif event.key == pygame.K_UP:
                for label in self.labels:
                    label.change_y(label.y + 30)
                self.scroller_rect.y -= 40

    def update(self):
        if self.scroller_rect.y < self.y + 10:
            self.scroller_rect.y = self.y + 10
        if self.scroller_rect.y > self.y + self.height - self.scroller_rect.height - 10:
            self.scroller_rect.y = self.y + self.height - self.scroller_rect.height - 10

    def draw(self, window: Window):
        pygame.draw.rect(window.screen, self.color, self.rect, 5)
        pygame.draw.rect(window.screen, self.scroller_color, self.scroller_rect, 15)
        for label in self.labels:
            if self.y + 30 <= label.y <= self.y + self.height - 30:
                label.show(window)
