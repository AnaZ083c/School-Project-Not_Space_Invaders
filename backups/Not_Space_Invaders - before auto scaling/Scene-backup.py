from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import Enemy, Enemies
from constants_and_globals import *
from Stars_classes import Star
from functions import *
from InputBox import *

import re
import random
import pygame


# font
# font = pygame.font.Font(FONT, 40)
# singleplayer_text = font.render('Single Player', True, TITANIUM_HWHITE)
# singleplayer_text_rect = singleplayer_text.get_rect()
# singleplayer_text_rect.center = (WIDTH/2 - singleplayer_text_rect.width/2, HEIGHT/2 - singleplayer_text_rect.height/2)
#
# multiplayer_text = font.render('Co-op', True, TITANIUM_HWHITE)
# options_text = font.render('Options', True, TITANIUM_HWHITE)
# exit_text = font.render('Exit', True, BLACK_RED)

joysticks = []
controller_chosen = False

def init_joysticks():
    global joysticks
    for i in range(pygame.joystick.get_count()):
        joysticks.append((pygame.joystick.Joystick(i), pygame.joystick.Joystick(i).get_instance_id()))
        pygame.joystick.Joystick(i).init()


stars = []
fall_speed = 15
for i in range(50):
    x = random.randint(1, WIDTH - 1)
    y = random.randint(1, HEIGHT - 1)
    fall_speed = random.randint(1, 16)
    width = 1
    height = width + fall_speed * 2

    star = Star(x, y, fall_speed, TITANIUM_HWHITE, width, height)
    stars.append(star)


def animate_stars(window: Window):
    global star
    for star in stars:
        star.draw(window)
        star.fall()
        star.check_if_i_should_reappear_on_top()


class Scene:
    def __init__(self, sprites: dict, texts: list = None):
        self.next = self
        self.sprites = sprites
        self.texts = texts

    def process_input(self, events, pressed_keys):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def show(self, window: Window):  # render
        raise NotImplementedError

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


class TitleScene(Scene):
    def __init__(self, sprites, texts):
        super().__init__(sprites, texts)
        self.heart_x = self.texts[0][1].x - 50
        self.heart_y = self.texts[0][1].y
        self.selected = 0
        self.min_select = 0
        self.max_select = 3
        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)
        self.next_scene = EnterNameP1(self.sprites, self.texts)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.texts[self.selected][1].y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.texts[self.selected][1].y

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    # Move to the next scene when the user pressed Enter
                    if self.selected == 0:
                        self.switch_to_scene(self.next_scene)
                    if self.selected == 3:
                        self.terminate()

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        window.screen.blit(self.texts[0][0], self.texts[0][1])  # draw Singleplayer text
        window.screen.blit(self.texts[1][0], self.texts[1][1])  # draw Multiplayer text
        window.screen.blit(self.texts[2][0], self.texts[2][1])  # draw Options text
        window.screen.blit(self.texts[3][0], self.texts[3][1])  # draw Exit text


class EnterNameP1(Scene):
    def __init__(self, sprites, text):
        super().__init__(sprites, text)
        self.selected = 8
        self.heart_x = self.texts[self.selected][1].x - 50
        self.heart_y = self.texts[self.selected][1].y
        self.min_select = 7
        self.max_select = 8
        self.next_scene = ChooseDevice(self.sprites, self.texts)
        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)
        self.isEmptyName = False

        self.font = pygame.font.Font(FONT, 60)
        self.input_box = InputBox(self.font, WIDTH/2 - 110, HEIGHT/2 - 20, 230, 60, 'Player 1')

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.texts[self.selected][1].y
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.texts[self.selected][1].y
                self.input_box.handle_event(event, self.selected == 8)

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    # Move to the next scene when the user pressed Enter
                    if self.selected == 8:
                        if self.isEmptyName:
                            self.switch_to_scene(self.next_scene)
                    if self.selected == 7:
                        self.switch_to_scene(TitleScene(self.sprites, self.texts))

    def update(self):
        # pass
        self.input_box.update()
        re_result = re.search("^[ ]*$|^.{0}$", self.input_box.text)
        self.isEmptyName = re_result is None  # if regex result is None, there were no matches

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        window.screen.blit(self.texts[9][0], self.texts[9][1])  # draw Description text
        window.screen.blit(self.texts[8][0], self.texts[8][1])  # draw Enter Name text
        self.input_box.draw(window.screen)

        window.screen.blit(self.texts[7][0], self.texts[7][1])  # draw Back text


class ChooseDevice(Scene):
    def __init__(self, sprites, texts):
        super().__init__(sprites, texts)
        self.selected = 5
        self.heart_x = self.texts[self.selected][1].x - 50
        self.heart_y = self.texts[self.selected][1].y
        self.min_select = 5
        self.max_select = 7
        self.next_scene = Singleplayer(self.sprites, self.texts)
        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        self.controller_selected = False

    def process_input(self, events, pressed_keys):
        global controller_chosen

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.texts[self.selected][1].y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.texts[self.selected][1].y

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    # Move to the next scene when the user pressed Enter
                    if self.selected == 5:
                        controller_chosen = True
                        self.switch_to_scene(ControllerInit(self.sprites, self.texts))
                    if self.selected == 6:
                        self.switch_to_scene(self.next_scene)

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        window.screen.blit(self.texts[4][0], self.texts[4][1])  # draw Description text

        window.screen.blit(self.texts[5][0], self.texts[5][1])  # draw Controller text
        window.screen.blit(self.texts[6][0], self.texts[6][1])  # draw Keyboard text

        window.screen.blit(self.texts[7][0], self.texts[7][1])  # draw Back text


class ControllerInit(Scene):
    def __init__(self, sprites, texts):
        super().__init__(sprites, texts)
        self.selected = 7
        self.heart_x = self.texts[self.selected][1].x - 50
        self.heart_y = self.texts[self.selected][1].y
        self.next_scene = Singleplayer(self.sprites, self.texts)

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        self.inited = 13

    def process_input(self, events, pressed_keys):
        global joysticks
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    # Move to the next scene when the user pressed Enter
                    if self.selected == 7:
                        self.switch_to_scene(ChooseDevice(self.sprites, self.texts))

            if event.type == pygame.JOYBUTTONDOWN:
                if event.joy == joysticks[0][1]:
                    if event.button == 0:  # if pressed A
                        self.switch_to_scene(self.next_scene)

    def update(self):
        init_joysticks()

        if not len(joysticks):
            self.inited = 13
        else:
            self.inited = 12

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        window.screen.blit(self.texts[10][0], self.texts[10][1])  # draw Description text
        window.screen.blit(self.texts[11][0], self.texts[11][1])  # draw Description continuation text

        window.screen.blit(self.texts[self.inited][0], self.texts[self.inited][1])  # draw Init/notInit controller

        window.screen.blit(self.texts[7][0], self.texts[7][1])  # draw Back text


class Singleplayer(Scene):
    def __init__(self, sprites, texts):
        super().__init__(sprites, texts)
        # self.player1 = Player(self.sprites["heart"], self.sprites["player1"],
        #                       image_size, HEIGHT-image_size, self.sprites["player_bullet"],
        #                       joysticks, 1, 1)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(TitleScene(self.sprites, self.texts))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

