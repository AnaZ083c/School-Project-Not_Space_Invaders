# from Window import Window
from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import Enemy, Enemies
from constants_and_globals import *
from Stars_classes import Star
from functions import *
from InputBox import InputBox
from Label import Label

import re
import random
import pygame


"""""""""""""""""""""""""""
    LABELS
"""""""""""""""""""""""""""
pygame.font.init()

# main menu
menu_font_size = int(60)
singleplayer_xy = (WIDTH/2, HEIGHT/2 - 60)
singleplayer_label = Label('Singleplayer', singleplayer_xy[0], singleplayer_xy[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', singleplayer_xy)

multiplayer_xy = (WIDTH/2, HEIGHT/2 + singleplayer_label.text.get_height() - 50)
multiplayer_label = Label('Multiplayer', multiplayer_xy[0], multiplayer_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', multiplayer_xy)

options_xy = (WIDTH/2, HEIGHT/2 + multiplayer_label.text.get_height()*2 - 40)
options_label = Label('Options', options_xy[0], options_xy[1],
                      TITANIUM_HWHITE, menu_font_size, FONT, 'center', options_xy)

exit_xy = (WIDTH/2, HEIGHT/2 + options_label.text.get_height()*3 - 30)
exit_label = Label('Exit', exit_xy[0], exit_xy[1],
                   TITANIUM_HWHITE, menu_font_size, FONT, 'center', exit_xy)

# # choose controlls menu
description_xy = (WIDTH/2, HEIGHT/2 - 200)
description_label = Label('Choose your device', description_xy[0], description_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_xy)

sp_controller_xy = (WIDTH/2, HEIGHT/2 - 60)
sp_controller_label = Label('Controller', sp_controller_xy[0], sp_controller_xy[1],
                            TITANIUM_HWHITE, menu_font_size, FONT, 'center', sp_controller_xy)

sp_keyboard_xy = (WIDTH/2, HEIGHT/2 + multiplayer_label.text.get_height() - 50)
sp_keyboard_label = Label('Keyboard', sp_keyboard_xy[0], sp_keyboard_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', sp_keyboard_xy)

back_xy = (WIDTH/2, HEIGHT/2 + exit_label.text.get_height()*3 - 30)
back_label = Label('Back', back_xy[0], back_xy[1],
                   TITANIUM_HWHITE, menu_font_size, FONT, 'center', back_xy)

# # Choose name menu
entername_xy = (WIDTH/2, HEIGHT/2 - 60)
entername_label = Label('Enter your name', entername_xy[0], entername_xy[1],
                        TITANIUM_HWHITE, menu_font_size, FONT, 'center', entername_xy)

description_xy2 = (WIDTH/2, HEIGHT/2 - 200)
description_label2 = Label('Choose your name', description_xy2[0], description_xy2[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_xy2)

# # Choose name menu 2 Players
description_xy4 = (WIDTH/2, HEIGHT/2 - 400)
description_label4 = Label('Choose your names', description_xy4[0], description_xy4[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_xy4)
entername_xy1 = (WIDTH/2, HEIGHT/2 - 190)
entername_label1 = Label('Player 1 enter your name', entername_xy1[0], entername_xy1[1],
                         PLAYER1_COLOR, menu_font_size, FONT, 'center', entername_xy1)
entername_xy2 = (WIDTH/2, HEIGHT/2 + 90)
entername_label2 = Label('Player 2 enter your name', entername_xy2[0], entername_xy2[1],
                         PLAYER2_COLOR, menu_font_size, FONT, 'center', entername_xy2)
back_xy2 = (WIDTH/2, HEIGHT/2 + exit_label.text.get_height()*3 + 250)
back_label2 = Label('Back', back_xy2[0], back_xy2[1],
                    TITANIUM_HWHITE, menu_font_size, FONT, 'center', back_xy2)


# # Choose device menu 2 Players
description_xy5 = (WIDTH/2, HEIGHT/2 - 400)
description_label5 = Label('Choose your devices', description_xy5[0], description_xy5[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_xy5)

p1_description_xy = (WIDTH/2, HEIGHT/2 - 300)
p1_description_label = Label('Player 1 ', p1_description_xy[0], p1_description_xy[1],
                             PLAYER1_COLOR, menu_font_size, FONT, 'center', p1_description_xy)
p1_controller_xy = (WIDTH/2, HEIGHT/2 - 160)
p1_controller_label = Label('Controller', p1_controller_xy[0], p1_controller_xy[1],
                            TITANIUM_HWHITE, menu_font_size, FONT, 'center', p1_controller_xy)
p1_keyboard_xy = (WIDTH/2, HEIGHT/2 - p1_controller_label.text.get_height() - 50)
p1_keyboard_label = Label('Keyboard', p1_keyboard_xy[0], p1_keyboard_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', p1_keyboard_xy)

p2_description_xy = (WIDTH/2, HEIGHT/2 + 50)
p2_description_label = Label('Player 2 ', p2_description_xy[0], p2_description_xy[1],
                             PLAYER2_COLOR, menu_font_size, FONT, 'center', p2_description_xy)
p2_controller_xy = (WIDTH/2, HEIGHT/2 + 190)
p2_controller_label = Label('Controller', p2_controller_xy[0], p2_controller_xy[1],
                            TITANIUM_HWHITE, menu_font_size, FONT, 'center', p2_controller_xy)
p2_keyboard_xy = (WIDTH/2, HEIGHT/2 + p2_controller_label.text.get_height() + 190)
p2_keyboard_label = Label('Keyboard', p2_keyboard_xy[0], p2_keyboard_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', p2_keyboard_xy)

continue_xy = (WIDTH/2, HEIGHT/2 + exit_label.text.get_height()*3 + 190)
continue_label = Label('Continue', continue_xy[0], continue_xy[1],
                       TITANIUM_HWHITE, menu_font_size, FONT, 'center', continue_xy)
# ------>  back_label2

# # Controller init menu
description_xy3 = (WIDTH/2, HEIGHT/2 - 200)
description_label3 = Label('Start your controller first', description_xy3[0], description_xy3[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_xy3)

description_cont_xy3 = (WIDTH/2, HEIGHT/2 - 140)
description_cont_label3 = Label('and press  A  to continue', description_cont_xy3[0], description_cont_xy3[1],
                                TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_cont_xy3)

inited_xy = (WIDTH/2, HEIGHT/2 - 10)
inited_label = Label('X', inited_xy[0], inited_xy[1],
                     (255, 0, 0), 80, FONT, 'center', inited_xy)

# # Controller init menu 2 Players
description_xy6 = (WIDTH/2, HEIGHT/2 - 400)
description_label6 = Label('Start your controllers first', description_xy6[0], description_xy6[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_xy6)
description_cont_xy6 = (WIDTH/2, HEIGHT/2 - 340)
description_cont_label6 = Label('and press  A  to continue', description_cont_xy6[0], description_cont_xy6[1],
                                TITANIUM_HWHITE, menu_font_size, FONT, 'center', description_cont_xy6)
player1_contr_xy = (WIDTH/2, HEIGHT/2 - 200)
player1_contr_label = Label('Player 1 ', player1_contr_xy[0], player1_contr_xy[1],
                            PLAYER1_COLOR, menu_font_size, FONT, 'center', player1_contr_xy)
inited_p1_xy = (WIDTH/2, HEIGHT/2 - player1_contr_label.text.get_height() - 70)
inited_p1_label = Label('X', inited_p1_xy[0], inited_p1_xy[1],
                        (255, 0, 0), 80, FONT, 'center', inited_p1_xy)

player2_contr_xy = (WIDTH/2, HEIGHT/2 + 100)
player2_contr_label = Label('Player 2 ', player2_contr_xy[0], player2_contr_xy[1],
                            PLAYER2_COLOR, menu_font_size, FONT, 'center', player2_contr_xy)
inited_p2_xy = (WIDTH/2, HEIGHT/2 + player2_contr_label.text.get_height() + 125)
inited_p2_label = Label('X', inited_p2_xy[0], inited_p2_xy[1],
                        (255, 0, 0), 80, FONT, 'center', inited_p2_xy)

# ------>  back_label2


# toggle sound label
sound_toggle_xy = (200, HEIGHT/2)
sound_toggle_label = Label("Music: {sound}".format(sound=sound_state), sound_toggle_xy[0], sound_toggle_xy[1],
                           (255, 255, 0), menu_font_size, FONT, 'center', sound_toggle_xy)

"""""""""""""""""""""""""""
    OTHER STUFF
"""""""""""""""""""""""""""
joysticks = set()
controller_chosen = False
p1_controller_chosen = False
p2_controller_chosen = False
p1_p2_controllers_chosen = [p1_controller_chosen, p2_controller_chosen]
is_multiplayer = False


def init_joysticks():
    global joysticks
    for i in range(pygame.joystick.get_count()):  # pygame.joystick.get_count()
        joysticks.add((pygame.joystick.Joystick(i), pygame.joystick.Joystick(i).get_instance_id()))
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


def get_sound_state(setting_file: str) -> int:
    # Read the file
    with open(setting_file, 'r') as file:
        current_state = file.read()

    return int(current_state)


menu_font_size = int(60)

player1_name = 'Player 1'
player2_name = 'Player 2'

player1_joyid = 0
player2_joyid = 0

"""""""""""""""""""""""""""
    CLASSES
"""""""""""""""""""""""""""
"""""""""""""""""""""""""""
    SCENE ABSTRACT
"""""""""""""""""""""""""""


class Scene:
    def __init__(self, sprites: dict):
        self.next = self
        self.sprites = sprites

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


"""""""""""""""""""""""""""
    TITLE SCENE
"""""""""""""""""""""""""""


class TitleScene(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        # create labels
        self.labels = [
            singleplayer_label,     # 0
            multiplayer_label,      # 1
            options_label,          # 2
            exit_label              # 3
        ]

        self.heart_x = self.labels[0].text_rect.x - 50
        self.heart_y = self.labels[0].text_rect.y
        self.selected = 0
        self.min_select = 0
        self.max_select = 3
        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

    def process_input(self, events, pressed_keys):
        global is_multiplayer

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.labels[self.selected].text_rect.y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.labels[self.selected].text_rect.y

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 0:  # Singleplayer
                        is_multiplayer = False
                        self.switch_to_scene(EnterNameP1(self.sprites))
                    if self.selected == 1:  # Multiplayer
                        is_multiplayer = True
                        self.switch_to_scene(EnterNameP2(self.sprites))
                    if self.selected == 3:  # Exit
                        self.terminate()

    def update(self):
        global sound_toggle_label
        current_sound_state = get_sound_state(SETTINGS)

        sound_toggle_label.update("Music: {sound}".format(sound=current_sound_state), (255, 255, 0))

    def show(self, window: Window):
        global sound_toggle_label

        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)     # draw Singleplayer text
        self.labels[1].show(window)     # draw Multiplayer text
        self.labels[2].show(window)     # draw Options text
        self.labels[3].show(window)     # draw Exit text
        sound_toggle_label.show(window)


"""""""""""""""""""""""""""
    ENTER NAME SCENE FOR SINGLEPLAYER
"""""""""""""""""""""""""""


class EnterNameP1(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.labels = [
            description_label2,     # 0
            entername_label,        # 1
            back_label              # 2
        ]

        self.selected = 1
        self.heart_x = self.labels[self.selected].text_rect.x - 50
        self.heart_y = self.labels[self.selected].text_rect.y
        self.min_select = 1
        self.max_select = 2

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)
        self.notEmptyName = False

        self.font = pygame.font.Font(FONT, 60)

        # if player_name[:-1] == ' ':

        self.input_box = InputBox(self.font, WIDTH/2 - 110, HEIGHT/2 - 20, 0, 60, player1_name, 'Player 1')

        print("player1_name =", player1_name)
        print("placeholder = ", self.input_box.placeholder)

    def process_input(self, events, pressed_keys):
        global player1_name

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.labels[self.selected].text_rect.y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.labels[self.selected].text_rect.y
                self.input_box.handle_event(event, self.selected == 1)

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 1:  # Enter name
                        if self.notEmptyName:
                            player1_name = self.input_box.text
                            print(player1_name)
                            self.switch_to_scene(ChooseDevice(self.sprites))
                    if self.selected == 2:  # Back
                        self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        # global player1_name
        self.input_box.update()
        re_result = re.search("^[ ]*$|^.{0}$", self.input_box.text)  # regex to check if input box is empty
        self.notEmptyName = re_result is None  # if regex result is None, there were no matches

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)         # draw Description text
        self.labels[1].show(window)         # draw Enter Name text
        self.input_box.draw(window.screen)
        self.labels[2].show(window)         # draw Back text


"""""""""""""""""""""""""""
    ENTER NAME SCENE FOR MULTIPLAYER
"""""""""""""""""""""""""""


class EnterNameP2(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.labels = [
            description_label4,      # 0
            entername_label1,        # 1
            entername_label2,        # 2
            back_label2              # 3
        ]

        self.selected = 1
        self.heart_x = self.labels[self.selected].text_rect.x - 50
        self.heart_y = self.labels[self.selected].text_rect.y
        self.min_select = 1
        self.max_select = 3

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)
        self.notEmptyNames = False

        self.font = pygame.font.Font(FONT, 60)
        self.input_box_p1 = InputBox(self.font, WIDTH/2 - 110, HEIGHT/2 - 150, 230, 60, player1_name)
        self.input_box_p2 = InputBox(self.font, WIDTH / 2 - 110, HEIGHT / 2 + 130, 230, 60, player2_name)

    def process_input(self, events, pressed_keys):
        global player1_name
        global player2_name

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.labels[self.selected].text_rect.y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.labels[self.selected].text_rect.y
                self.input_box_p1.handle_event(event, self.selected == 1)
                self.input_box_p2.handle_event(event, self.selected == 2)

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 1:  # Enter name P1
                        if self.notEmptyNames:
                            player1_name = self.input_box_p1.text
                            player2_name = self.input_box_p2.text
                            self.switch_to_scene(ChooseDeviceP2(self.sprites))
                    if self.selected == 2:  # Enter name P2
                        if self.notEmptyNames:
                            player1_name = self.input_box_p1.text
                            player2_name = self.input_box_p2.text
                            self.switch_to_scene(ChooseDeviceP2(self.sprites))
                    if self.selected == 3:  # Back
                        self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        self.input_box_p1.update()
        self.input_box_p2.update()
        re_result_p1 = re.search("^[ ]*$|^.{0}$|^\n$", self.input_box_p1.text)  # regex to check if input box is empty
        re_result_p2 = re.search("^[ ]*$|^.{0}$|^\n$", self.input_box_p2.text)
        self.notEmptyNames = (re_result_p1 is None) and (re_result_p2 is None)  # if regex result is None, there were no matches

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)         # draw Description text
        self.labels[1].show(window)         # draw Player 1 Enter Name text
        self.input_box_p1.draw(window.screen)

        self.labels[2].show(window)         # draw Player 2 Enter Name text
        self.input_box_p2.draw(window.screen)

        self.labels[3].show(window)         # draw Back text


"""""""""""""""""""""""""""
    DEVICE SELECT SCENE FOR MULTIPLAYER
"""""""""""""""""""""""""""


class ChooseDeviceP2(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.labels = [
            description_label5,     # 0  not selectable
            p1_description_label,   # 1  not selectable

            p1_controller_label,    # 2
            p1_keyboard_label,      # 3

            p2_description_label,   # 4  not selectable

            p2_controller_label,    # 5
            p2_keyboard_label,      # 6

            continue_label,         # 7
            back_label2             # 8
        ]

        self.labels[2].update('Controller', TITANIUM_HWHITE)
        self.labels[3].update('Keyboard', TITANIUM_HWHITE)
        self.labels[5].update('Controller', TITANIUM_HWHITE)
        self.labels[6].update('Keyboard', TITANIUM_HWHITE)

        self.selected = 2
        self.heart_x = self.labels[self.selected].text_rect.x - 50
        self.heart_y = self.labels[self.selected].text_rect.y
        self.min_select = 2
        self.max_select = 8
        self.not_selectable = 4

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        self.controller_selected = False

        global controller_chosen
        global p1_controller_chosen
        global p2_controller_chosen
        global p1_p2_controllers_chosen

        p1_controller_chosen = False
        p2_controller_chosen = False
        controller_chosen = False
        p1_p2_controllers_chosen = [None, None]

    def process_input(self, events, pressed_keys):
        global controller_chosen
        global p1_controller_chosen
        global p2_controller_chosen
        global p1_p2_controllers_chosen
        global player1_joyid
        global player2_joyid

        print(p1_p2_controllers_chosen)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                    self.selected += 1
                    if self.selected == self.not_selectable:
                        self.selected += 1
                    if self.selected > self.max_select:
                        self.selected = self.max_select
                    self.heart_y = self.labels[self.selected].text_rect.y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected == self.not_selectable:
                        self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.labels[self.selected].text_rect.y

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 2:  # player 1 Controller
                        controller_chosen = True
                        p1_p2_controllers_chosen[0] = True
                        player1_joyid = 0
                        self.labels[2].update('Controller', TITANIUM_HWHITE)
                        self.labels[3].update('Keyboard', NOT_CHOSEN)
                        # self.switch_to_scene(ControllerInit(self.sprites))
                    if self.selected == 3:  # player 1 Keyboard
                        p1_p2_controllers_chosen[0] = False
                        player1_joyid = -1
                        self.labels[2].update('Controller', NOT_CHOSEN)
                        self.labels[3].update('Keyboard', TITANIUM_HWHITE)
                        # self.switch_to_scene(Singleplayer(self.sprites))
                    if self.selected == 5:  # player 2 Controller
                        p1_p2_controllers_chosen[1] = True
                        if player2_joyid < 0:
                            player2_joyid = 0
                        else:
                            player2_joyid = 1
                        self.labels[5].update('Controller', TITANIUM_HWHITE)
                        self.labels[6].update('Keyboard', NOT_CHOSEN)
                    if self.selected == 6:  # player 2 Keyboard
                        p1_p2_controllers_chosen[1] = False
                        player2_joyid = -1
                        self.labels[5].update('Controller', NOT_CHOSEN)
                        self.labels[6].update('Keyboard', TITANIUM_HWHITE)
                    if self.selected == 7:
                        if not (None in p1_p2_controllers_chosen):
                            if sum(p1_p2_controllers_chosen) == 0:  # both chose Keyboard
                                self.switch_to_scene(Multiplayer(self.sprites))
                            else:
                                self.switch_to_scene(ControllerInitP2(self.sprites))
                    if self.selected == 8:  # Back
                        self.switch_to_scene(EnterNameP2(self.sprites))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)     # draw Description text
        self.labels[1].show(window)     # draw Player 1 description text
        self.labels[2].show(window)     # draw Player 1 controller
        self.labels[3].show(window)     # draw Player 1 keyboard
        self.labels[4].show(window)     # draw Player 2 description text
        self.labels[5].show(window)     # draw Player 2 controller
        self.labels[6].show(window)     # draw Player 2 keyboard
        self.labels[7].show(window)     # draw Continue
        self.labels[8].show(window)     # draw Back


"""""""""""""""""""""""""""
    INIT CONTROLLER SCENE FOR MULTIPLAYER
"""""""""""""""""""""""""""


class ControllerInitP2(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.labels = [
            description_label6,         # 0
            description_cont_label6,    # 1

            player1_contr_label,        # 2
            inited_p1_label,            # 3

            player2_contr_label,        # 4
            inited_p2_label,            # 5
            back_label2                 # 6
        ]

        self.selected = 6
        self.heart_x = self.labels[self.selected].text_rect.x - 50
        self.heart_y = self.labels[self.selected].text_rect.y
        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        global p1_p2_controllers_chosen
        if not p1_p2_controllers_chosen[0]:
            self.labels[3].change_size(60)
            self.labels[3].update('Keyboard', TITANIUM_HWHITE)
        elif p1_p2_controllers_chosen[0]:
            self.labels[3].change_size(80)
            self.labels[3].update('X', (255, 0, 0))

        if not p1_p2_controllers_chosen[1]:
            self.labels[5].change_size(60)
            self.labels[5].update('Keyboard', TITANIUM_HWHITE)
        elif p1_p2_controllers_chosen[1]:
            self.labels[5].change_size(80)
            self.labels[5].update('X', (255, 0, 0))

        self.confirmed = 0

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
                    if self.selected == 6:  # Back
                        self.switch_to_scene(ChooseDeviceP2(self.sprites))

            if event.type == pygame.JOYBUTTONDOWN:
                self.confirm.play()
                if event.joy == list(joysticks)[0][1]:
                    if event.button == 0:  # if Player 1 pressed A
                        self.confirmed += 1
                        if self.confirmed == sum(p1_p2_controllers_chosen):
                            self.switch_to_scene(Multiplayer(self.sprites))
                if len(joysticks) > 1:
                    if event.joy == list(joysticks)[1][1]:
                        if event.button == 0:  # if Player 2 pressed A
                            self.confirmed += 1
                            if self.confirmed == sum(p1_p2_controllers_chosen):
                                self.switch_to_scene(Multiplayer(self.sprites))

    def update(self):
        init_joysticks()
        print(joysticks)

        if not len(joysticks):
            if self.labels[3].string != 'Keyboard':
                self.labels[3].update('X', (255, 0, 0))
            if self.labels[5].string != 'Keyboard':
                self.labels[5].update('X', (255, 0, 0))
        elif len(joysticks) == 1:
            if self.labels[3].string != 'Keyboard':
                self.labels[3].update('O', (0, 255, 0))
            elif self.labels[5].string != 'Keyboard':
                self.labels[5].update('O', (0, 255, 0))
        elif len(joysticks) == 2:
            if self.labels[3].string != 'Keyboard':
                self.labels[3].update('O', (0, 255, 0))
            if self.labels[5].string != 'Keyboard':
                self.labels[5].update('O', (0, 255, 0))

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)
        self.labels[1].show(window)
        self.labels[2].show(window)
        self.labels[3].show(window)
        self.labels[4].show(window)
        self.labels[5].show(window)
        self.labels[6].show(window)


"""""""""""""""""""""""""""
    DEVICE SELECT SCENE FOR SINGLEPLAYER
"""""""""""""""""""""""""""


class ChooseDevice(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.labels = [
            description_label,      # 0
            sp_controller_label,    # 1
            sp_keyboard_label,      # 2
            back_label              # 3
        ]

        self.selected = 1
        self.heart_x = self.labels[self.selected].text_rect.x - 50
        self.heart_y = self.labels[self.selected].text_rect.y
        self.min_select = 1
        self.max_select = 3

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
                    self.heart_y = self.labels[self.selected].text_rect.y
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                    self.selected -= 1
                    if self.selected < self.min_select:
                        self.selected = self.min_select
                    self.heart_y = self.labels[self.selected].text_rect.y

                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 1:  # Controller
                        controller_chosen = True
                        self.switch_to_scene(ControllerInit(self.sprites))
                    if self.selected == 2:  # Keyboard
                        self.switch_to_scene(Singleplayer(self.sprites))
                    if self.selected == 3:  # Back
                        self.switch_to_scene(EnterNameP1(self.sprites))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)     # draw Description text
        self.labels[1].show(window)     # draw Controller text
        self.labels[2].show(window)     # draw Keyboard text
        self.labels[3].show(window)     # draw Back text


"""""""""""""""""""""""""""
    INIT CONTROLLER SCENE FOR SINGLEPLAYER
"""""""""""""""""""""""""""


class ControllerInit(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.labels = [
            description_label3,         # 0
            description_cont_label3,    # 1
            inited_label,               # 2
            back_label                  # 3
        ]

        self.selected = 3
        self.heart_x = self.labels[self.selected].text_rect.x - 50
        self.heart_y = self.labels[self.selected].text_rect.y

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

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
                    if self.selected == 3:
                        self.switch_to_scene(ChooseDevice(self.sprites))

            if event.type == pygame.JOYBUTTONDOWN:
                if event.joy == list(joysticks)[0][1]:
                    if event.button == 0:  # if pressed A
                        self.switch_to_scene(Singleplayer(self.sprites))

    def update(self):
        init_joysticks()

        if not len(joysticks):
            self.labels[2].update('X', (255, 0, 0))
        else:
            self.labels[2].update('O', (0, 255, 0))

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)
        self.labels[1].show(window)
        self.labels[2].show(window)
        self.labels[3].show(window)


"""""""""""""""""""""""""""
    SINGLEPLAYER GAME SCENE
"""""""""""""""""""""""""""


class Singleplayer(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        # self.player1 = Player(self.sprites["heart"], self.sprites["player1"],
        #                       image_size, HEIGHT-image_size, self.sprites["player_bullet"],
        #                       joysticks, 1, 1)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)


"""""""""""""""""""""""""""
    MULTIPLAYER GAME SCENE
"""""""""""""""""""""""""""


class Multiplayer(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        # self.player1 = Player(self.sprites["heart"], self.sprites["player1"],
        #                       image_size, HEIGHT-image_size, self.sprites["player_bullet"],
        #                       joysticks, 1, 1)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)


"""""""""""""""""""""""""""
    UNIVERSAL GAME SCENE
"""""""""""""""""""""""""""


class GameScene(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        self.joysticks_list = list(joysticks)

        self.player1_animation = Animation(self.sprites["player1"], 500)
        self.player2_animation = Animation(self.sprites["player2"], 500)

        self.player1 = Player(self.sprites["heart"],
                              self.sprites["player1"],
                              image_size,
                              HEIGHT-image_size,
                              self.sprites["player_bullet"],
                              1)

        self.player2 = Player(self.sprites["heart"],
                              self.sprites["player2"],
                              image_size,
                              HEIGHT - image_size,
                              self.sprites["player_bullet"],
                              2)

        global p1_p2_controllers_chosen
        if p1_p2_controllers_chosen[0]:
            self.player1.joysticks = self.joysticks_list
            self.player1.joystick_index = 0
        if p1_p2_controllers_chosen[1]:
            self.player2.joysticks = self.joysticks_list
            self.player2.joysticks_index = 1

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)
