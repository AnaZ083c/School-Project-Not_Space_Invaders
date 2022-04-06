from constants_and_globals import *
import pygame as pg


class InputBox:
    def __init__(self, font, x, y, w, h, text='', placeholder='Player 1'):
        self.font = font
        self.x = x
        self.y = y
        self.w = w * scale
        self.h = h * scale
        self.rect = pg.Rect(self.x, self.y, self.w, self.h)
        self.placeholder = placeholder

        # self.rect.center = (self.x, self.y)
        self.color = TITANIUM_HWHITE
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, selected):
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     # If the user clicked on the input_box rect.
        #     if self.rect.collidepoint(event.pos):
        #         # Toggle the active variable.
        #         self.active = not self.active
        #     else:
        #         self.active = False
        #     # Change the current color of the input box.
        self.active = selected
        self.color = TITANIUM_HWHITE if self.active else TITANIUM_HWHITE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) <= len(self.placeholder)-1:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        # width = max(200, self.txt_surface.get_width()+10)
        width = self.txt_surface.get_width()+10
        self.rect.w = width
        self.rect.x = WIDTH/2 - width/2

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
