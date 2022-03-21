from Sprite import SpriteSheet, Sprite, Animation
from Player_classes import Player, Bullet
from Enemy_classes import Enemy, Enemies, FirstBoss, SecondBoss, ThirdBoss, FourthBoss, FinalBoss
from constants_and_globals import *
from Stars_classes import Star
from functions import *
from InputBox import InputBox
from ScrollBox import ScrollBox
from Label import Label
from Pickup import *

import re
import random
import pygame


"""""""""""""""""""""""""""
    LABELS
"""""""""""""""""""""""""""
pygame.font.init()

# main menu
title_size = int(100)
title_xy = (WIDTH/2, HEIGHT/2 - 250)
title_label = Label('totally NOT Space Invaders', title_xy[0], title_xy[1],
                    (255, 230, 0), title_size, FONT, 'center', title_xy)

menu_font_size = int(60)
singleplayer_xy = (WIDTH/2, HEIGHT/2 - 60)
singleplayer_label = Label('Singleplayer', singleplayer_xy[0], singleplayer_xy[1],
                           TITANIUM_HWHITE, menu_font_size, FONT, 'center', singleplayer_xy)

multiplayer_xy = (WIDTH/2, HEIGHT/2 + singleplayer_label.text.get_height() - 50)
multiplayer_label = Label('Multiplayer', multiplayer_xy[0], multiplayer_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', multiplayer_xy)

options_xy = (WIDTH/2, HEIGHT/2 + multiplayer_label.text.get_height()*2 - 40)
options_label = Label('Points', options_xy[0], options_xy[1],
                      TITANIUM_HWHITE, menu_font_size, FONT, 'center', options_xy)

controls_xy = (WIDTH/2, HEIGHT/2 + options_label.text.get_height()*3 - 30)
controls_label = Label('Controls', controls_xy[0], controls_xy[1],
                       TITANIUM_HWHITE, menu_font_size, FONT, 'center', controls_xy)

exit_xy = (WIDTH/2, HEIGHT/2 + controls_label.text.get_height()*4 - 20)
exit_label = Label('Exit', exit_xy[0], exit_xy[1],
                   TITANIUM_HWHITE, menu_font_size, FONT, 'center', exit_xy)

# # Points menu
points_title_xy = (WIDTH/2, HEIGHT/2 - 360)
points_title = Label('Points', points_title_xy[0], points_title_xy[1],
                     TITANIUM_HWHITE, menu_font_size, FONT, 'center', points_title_xy)

back_points_xy = (WIDTH/2, HEIGHT/2 + exit_label.text.get_height()*7 - 30)
back_points_label = Label('Back', back_points_xy[0], back_points_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', back_points_xy)

# # Controls menu
controls_title_xy = (WIDTH/2, HEIGHT/2 - 360)
controls_title = Label('Controls', controls_title_xy[0], controls_title_xy[1],
                       TITANIUM_HWHITE, menu_font_size, FONT, 'center', controls_title_xy)

back_controls_xy = (WIDTH/2, HEIGHT/2 + exit_label.text.get_height()*7 - 30)
back_controls_label = Label('Back', back_points_xy[0], back_points_xy[1],
                          TITANIUM_HWHITE, menu_font_size, FONT, 'center', back_points_xy)

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

slow_stars = []
fall_speed = 5
for i in range(50):
    x = stars[i].x
    y = stars[i].y
    fall_speed = random.randint(1, 16)
    width = 1
    height = width + fall_speed * 2

    slow_star = Star(x, y, fall_speed, TITANIUM_HWHITE, 1, 1)
    slow_stars.append(slow_star)


def animate_stars(window: Window):
    global star
    for star in stars:
        star.draw(window)
        star.fall()
        star.check_if_i_should_reappear_on_top()

def animate_slow_stars(window: Window):
    global slow_star
    for slow_star in slow_stars:
        slow_star.draw(window)
        slow_star.fall()
        slow_star.check_if_i_should_reappear_on_top()



def get_sound_state(setting_file: str) -> int:
    # Read the file
    with open(setting_file, 'r') as file:
        current_state = file.read()

    return int(current_state)


player1_name = 'Player 1'
player2_name = 'Player 2'

player1_joyid = 0
player2_joyid = 0

player1_controls = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "fire": pygame.K_KP_ENTER,
    "dash": pygame.K_KP3
}

player1_controls_controller = {
    "up": [pygame.K_UP, "L pad"],
    "down": [pygame.K_DOWN, "L pad"],
    "left": [pygame.K_LEFT, "L pad"],
    "right": [pygame.K_RIGHT, "L pad"],
    "fire": [pygame.K_KP_ENTER, "A"],
    "dash": [pygame.K_KP3, "RB"],
    "pause": [pygame.K_F10, ""]
}

player2_controls_controller = {
    "up": [pygame.K_w, "L pad"],
    "down": [pygame.K_s, "L pad"],
    "left": [pygame.K_a, "L pad"],
    "right": [pygame.K_d, "L pad"],
    "fire": [pygame.K_k, "A"],
    "dash": [pygame.K_SPACE, "RB"],
    "pause": [pygame.K_F10, ""]
}

player2_controls = {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d,
    "fire": pygame.K_k,
    "dash": pygame.K_SPACE
}

menu_font_size = int(60)
level = 1
wave = 1
lvl_file = LEVELS + 'level' + str(level) + '_' + str(wave) + '.ens'
boss_time = False

killed = 0
skipped = 0


def update_level():
    global level
    global wave
    global lvl_file
    level += 1
    lvl_file = LEVELS + 'level' + str(level) + '_' + str(wave) + '.ens'


def update_wave():
    global level
    global wave
    global lvl_file
    wave += 1
    if wave > 3:
        wave = 1
        update_level()
    lvl_file = LEVELS + 'level' + str(level) + '_' + str(wave) + '.ens'


def reset_wave():
    global level
    global wave
    global lvl_file
    wave = 1
    lvl_file = LEVELS + 'level' + str(level) + '_' + str(wave) + '.ens'


def reset_level():
    global level
    global wave
    global lvl_file
    level = 1
    lvl_file = LEVELS + 'level' + str(level) + '_' + str(wave) + '.ens'


def reset_level_wave():
    global level
    global wave
    global lvl_file
    level = 1
    wave = 1
    lvl_file = LEVELS + 'level' + str(level) + '_' + str(wave) + '.ens'


def delay(delay_time, timer, start_time):
    current_time = pygame.time.get_ticks()
    while current_time - start_time < delay_time:
        timer += 1
    return True


# ingame
new_level_wave_font_size = int(80)
new_lw_xy = (WIDTH/2, HEIGHT/2 - 80)
new_lw_label = Label("Level " + str(level) + ": wave " + str(wave) + " of 3", new_lw_xy[0], new_lw_xy[1],
                     (255, 255, 0), new_level_wave_font_size, FONT, 'center', new_lw_xy)

boss_font_size = int(80)
boss_label_xy = (WIDTH/2, HEIGHT/2 - 80)
boss_label = Label("BOSS num. " + str(level), boss_label_xy[0], boss_label_xy[1],
                   (255, 255, 0), boss_font_size, FONT, 'center', boss_label_xy)

pause_font_size = int(90)
pause_label_xy = (WIDTH/2, HEIGHT/2 - 80)
pause_label = Label("PAUSED", pause_label_xy[0], pause_label_xy[1],
                   (255, 200, 0), pause_font_size, FONT, 'center', pause_label_xy)


death_font_size = int(100)
death_label_xy = (WIDTH/2, HEIGHT/2 - 80)
death_label = Label("OUR PLANET IS DOOMED!", death_label_xy[0], death_label_xy[1],
                    (255, 0, 0), death_font_size, FONT, 'center', death_label_xy)

win_font_size = int(100)
win_label_xy = (WIDTH/2, HEIGHT/2 - 80)
win_label = Label("OUR PLANET IS SAVED!", win_label_xy[0], win_label_xy[1],
                  (0, 255, 0), win_font_size, FONT, 'center', win_label_xy)


def create_leadboard(points_path):
    labels = []
    font_size = int(60)
    factor = 5
    label_x = WIDTH/2
    label_y = HEIGHT/2 - factor
    mult = 1

    f = open(points_path, "r")
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        label = Label(line, label_x, label_y,
                      TITANIUM_HWHITE, font_size, FONT, 'center', (label_x, label_y))
        # print(line)
        labels.append(label)
        factor -= 10
        label_y = HEIGHT / 2 + labels[0].text.get_height() * mult - factor
        mult += 1

    f.close()
    return labels

def create_controls_labels(p1_controls: dict, p2_controls: dict):
    labels = []

    font_size = int(60)
    factor = 5
    label_x = WIDTH/2
    label_y = HEIGHT/2 - factor
    mult = 1

    player1_labels = [
        Label("Controls for PLayer 1", label_x, label_y,
              PLAYER1_COLOR, font_size, FONT, 'center', (label_x, label_y))
    ]
    factor -= 10
    label_y = HEIGHT / 2 + player1_labels[0].text.get_height() * mult - factor
    mult += 1
    for name in p1_controls.keys():
        control_keyboard = pygame.key.name(p1_controls[name][0])
        control_keyboard = control_keyboard.replace("[", "").replace("]", "")
        control_controller = p1_controls[name][1]
        # print(control_keyboard)
        label = Label(f"{str(name)} ..... {control_keyboard}, {control_controller}", label_x, label_y,
                      TITANIUM_HWHITE, font_size, FONT, 'center', (label_x, label_y))
        player1_labels.append(label)
        factor -= 10
        label_y = HEIGHT / 2 + player1_labels[0].text.get_height() * mult - factor
        mult += 1

    factor -= 10
    label_y = HEIGHT / 2 + player1_labels[0].text.get_height() * mult - factor
    mult += 1
    player2_labels = [
        Label("Controls for PLayer 2", label_x, label_y,
              PLAYER2_COLOR, font_size, FONT, 'center', (label_x, label_y))
    ]
    factor -= 10
    label_y = HEIGHT / 2 + player2_labels[0].text.get_height() * mult - factor
    mult += 1
    for name in p2_controls.keys():
        control_keyboard = pygame.key.name(p2_controls[name][0])
        control_controller = p2_controls[name][1]
        label = Label(f"{str(name)} ..... {control_keyboard}, {control_controller}", label_x, label_y,
                      TITANIUM_HWHITE, font_size, FONT, 'center', (label_x, label_y))
        player2_labels.append(label)
        factor -= 10
        label_y = HEIGHT / 2 + player2_labels[0].text.get_height() * mult - factor
        mult += 1

    labels = player1_labels + player2_labels
    return labels


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
            title_label,            # 0
            singleplayer_label,     # 1
            multiplayer_label,      # 2
            options_label,          # 3
            controls_label,         # 4
            exit_label              # 5
        ]

        self.heart_x = self.labels[1].text_rect.x - 50
        self.heart_y = self.labels[1].text_rect.y
        self.selected = 1
        self.min_select = 1
        self.max_select = 5
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
                    if self.selected == 1:  # Singleplayer
                        is_multiplayer = False
                        self.switch_to_scene(EnterNameP1(self.sprites))
                    if self.selected == 2:  # Multiplayer
                        is_multiplayer = True
                        self.switch_to_scene(EnterNameP2(self.sprites))
                    if self.selected == 3:  # Points
                        self.switch_to_scene(PointsScene(self.sprites))
                    if self.selected == 4:  # Controls
                        self.switch_to_scene(ControlsScene(self.sprites))
                    if self.selected == 5:  # Exit
                        self.terminate()

    def update(self):
        pass
        # global sound_toggle_label
        # current_sound_state = get_sound_state(SETTINGS)
        #
        # sound_toggle_label.update("Music: {sound}".format(sound=current_sound_state), (255, 255, 0))

    def show(self, window: Window):
        # global sound_toggle_label

        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.labels[0].show(window)     # draw Title text
        self.labels[1].show(window)     # draw Singleplayer text
        self.labels[2].show(window)     # draw Multiplayer text
        self.labels[3].show(window)     # draw Points text
        self.labels[4].show(window)     # draw Controls text
        self.labels[5].show(window)     # draw Exit text
        # sound_toggle_label.show(window)


"""""""""""""""""""""""""""
    POINTS SCENE
"""""""""""""""""""""""""""


class PointsScene(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        # create labels
        self.other_labels = [
            points_title,       # 0
            back_points_label   # 1
        ]
        self.labels = create_leadboard(POINTS)

        self.selected = 1
        self.heart_x = self.other_labels[self.selected].text_rect.x - 50
        self.heart_y = self.other_labels[self.selected].text_rect.y

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        scroll_box_width = 800
        scroll_box_height = 600
        scroll_box_x = self.labels[0].x - 5 - scroll_box_width/2
        scroll_box_y = self.labels[0].y - 5 - scroll_box_height/2
        self.scroll_box = ScrollBox(self.labels, scroll_box_x, scroll_box_y, scroll_box_width, scroll_box_height)

    def process_input(self, events, pressed_keys):
        for event in events:
            self.scroll_box.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 1:
                        self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        self.scroll_box.update()

    def show(self, window: Window):
        # global sound_toggle_label

        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.scroll_box.draw(window)
        self.other_labels[0].show(window)
        self.other_labels[1].show(window)


"""""""""""""""""""""""""""
    CONTROLS SCENE
"""""""""""""""""""""""""""


class ControlsScene(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        # create labels
        self.other_labels = [
            controls_title,       # 0
            back_controls_label   # 1
        ]
        self.labels = create_controls_labels(player1_controls_controller, player2_controls_controller)

        self.selected = 1
        self.heart_x = self.other_labels[self.selected].text_rect.x - 50
        self.heart_y = self.other_labels[self.selected].text_rect.y

        self.selector_sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.confirm = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        scroll_box_width = 800
        scroll_box_height = 600
        scroll_box_x = self.labels[0].x - 5 - scroll_box_width/2
        scroll_box_y = self.labels[0].y - 5 - scroll_box_height/2
        self.scroll_box = ScrollBox(self.labels, scroll_box_x, scroll_box_y, scroll_box_width, scroll_box_height)

    def process_input(self, events, pressed_keys):
        for event in events:
            self.scroll_box.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selector_sfx.play()
                if event.key == pygame.K_UP:
                    self.selector_sfx.play()
                if event.key == pygame.K_RETURN:
                    self.confirm.play()
                    if self.selected == 1:
                        self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        self.scroll_box.update()

    def show(self, window: Window):
        # global sound_toggle_label

        window.screen.fill(BLACK)
        animate_stars(window)

        window.screen.blit(self.sprites["heart"].frames[0], (self.heart_x, self.heart_y))
        self.scroll_box.draw(window)
        self.other_labels[0].show(window)
        self.other_labels[1].show(window)


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

        # print("player1_name =", player1_name)
        # print("placeholder = ", self.input_box.placeholder)

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
                            # print(player1_name)
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

        # print(p1_p2_controllers_chosen)

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
        # print(joysticks)

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
        global player1_joyid

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
                        player1_joyid = -1
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


current_boss = 0


"""""""""""""""""""""""""""
    SINGLEPLAYER GAME SCENE
"""""""""""""""""""""""""""


class Singleplayer(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.max_points = create_random_levels()

        global level
        global wave
        level = 1
        wave = 1

        global joysticks
        self.heart_img_size = FRAME_OFFSET * self.sprites["heart"].scale
        self.death_img_size = FRAME_OFFSET * self.sprites["death"].scale
        self.win_img_size = FRAME_OFFSET * self.sprites["win"].scale

        self.boom_animation = Animation(self.sprites["explosion"], 200)

        self.enemy_bullets = [
            self.sprites["enemy_bullet"],
            self.sprites["enemy-purple-bullet"],
            self.sprites["enemy-blue-bullet"],
            self.sprites["enemy-yellow-bullet"]
        ]

        self.player_bullets = [
            self.sprites["player-purple-bullet"],
            self.sprites["player-blue-bullet"],
            self.sprites["player-yellow-bullet"],
            self.sprites["player-green-bullet"],
            self.sprites["player_bullet"]
        ]

        global player1_name
        self.p1_title_label = Label(player1_name, self.heart_img_size - 40, 15, PLAYER1_COLOR, 40, FONT)
        self.p1_points_label = Label(str(0), self.heart_img_size, 80, TITANIUM_HWHITE, 40, FONT,
                                     'topleft',
                                     (self.heart_img_size, 80))

        self.player1 = Player(self.p1_points_label, self.sprites["dash-left-right"], self.sprites["dash-up-down"], self.sprites["explosion"], self.sprites["fuel-fire"], self.sprites["heart"], self.sprites["player1"],
                              image_size, HEIGHT-image_size, self.sprites["player_bullet"],
                              1, list(joysticks), player1_joyid)
        self.player1.set_controls(player1_controls)


        self.enemies = read_enemies(lvl_file, self.sprites["enemies"], self.sprites["explosion"], self.enemy_bullets, 150, 80)
        self.pressed_keys = None

        self.enemy_explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)
        self.hidden = 0

        self.killed_hidden = []  # [None] * len(self.enemies)
        self.killed_animations = []
        self.boss_killed_animation = []
        self.timer_level = 0
        self.last_update = pygame.time.get_ticks()
        self.timer = 0
        self.cooldown = 100

        self.switch_level = False
        self.new_set_label = new_lw_label
        self.boss_label = boss_label
        self.enemies_num = len(self.enemies)

        self.bosses = [
            FirstBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["first-boss"], WIDTH / 2, HEIGHT / 4, self.enemy_bullets[0], 70.0),
            SecondBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["second-boss"], WIDTH / 2, HEIGHT / 4, self.enemy_bullets[1], 65.0),
            ThirdBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["third-boss"], WIDTH / 2, HEIGHT / 4, self.enemy_bullets[2], 55.0),
            FourthBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["fourth-boss"], WIDTH / 2, HEIGHT / 4, self.enemy_bullets[3], 50.0),
            FinalBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["final-boss"], WIDTH / 2, HEIGHT / 4, self.enemy_bullets[1], 45.0),
        ]

        self.pickups = [
            Pickup(self.sprites["green-pickup"], 5.0, 1.5, 0, "green", self.player_bullets[3], 2),
            Pickup(self.sprites["purple-pickup"], 3.0, 2.0, 0, "purple", self.player_bullets[0], 3),
            Pickup(self.sprites["blue-pickup"], 10.0, 3.0, 0, "blue", self.player_bullets[1], 4),
            Pickup(self.sprites["yellow-pickup"], 8.0, 2.5, 0, "yellow", self.player_bullets[2], 5),
            Pickup(self.sprites["red-pickup"], 8.0, 2.5, 0, "red", self.player_bullets[4], 1),
        ]

        self.constant_pickups = [
            Pickup(self.sprites["red-pickup"], 8.0, 2.5, 0, "red", self.player_bullets[4], 1),
            Pickup(self.sprites["heal-pickup"], 9.0, 3.5, 3, "heal", None)
        ]

        self.boss_time = False
        self.show_boss_label = False
        self.show_last_boss_bar = False
        self.killed_boss = False
        self.pause = False
        self.pause_label = pause_label

        self.game_over = False
        self.win = False

    def process_input(self, events, pressed_keys):
        global current_boss

        self.pressed_keys = pressed_keys
        for event in events:
            if not self.pause:
                if self.player1.health > 0:
                    self.player1.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    self.pause = not self.pause

        if self.game_over:
            save_points(POINTS, [[self.player1, player1_name]])
            self.switch_to_scene(DeathScene(self.sprites))

        if self.win:
            save_points(POINTS, [[self.player1, player1_name]])
            self.switch_to_scene(DeathScene(self.sprites))

    def update(self):
        if not self.pause:
            global current_boss

            current_time = pygame.time.get_ticks()
            if self.switch_level:
                if current_time - self.last_update >= self.cooldown:
                    self.timer += 1
                    self.last_update = current_time
                    if self.timer >= self.cooldown:
                        if self.boss_time:
                            self.timer = 0
                            # print("BOSS")
                            self.show_boss_label = False

                        else:
                            self.enemies = read_enemies(lvl_file, self.sprites["enemies"], self.sprites["explosion"], self.enemy_bullets, 150, 80)
                            self.show_last_boss_bar = False
                            self.killed_hidden = []
                            self.killed_animations = []
                            self.boss_killed_animation = []
                            self.enemies_num = len(self.enemies)
                            # print("NEXT LEVEL !!")
                            self.timer = 0
                            self.switch_level = False

            en_bullets = []
            for enemy in self.enemies:
                en_bullets += enemy.en_bullets

            if not self.show_boss_label and self.boss_time:
                en_bullets += self.bosses[current_boss].en_bullets

            self.player1.update(self.pressed_keys, en_bullets, self.pickups + self.constant_pickups)
            # self.p1_points_label.update(str(self.player1.points), TITANIUM_HWHITE)

            # boss update
            if not self.show_boss_label and self.boss_time:
                self.bosses[current_boss].update(self.player1.bullets)

            if self.bosses[current_boss].helth <= 0:
                # self.bosses[0].defeated = True
                self.last_update = pygame.time.get_ticks()
                self.boss_killed_animation.append([Animation(self.sprites["boss-explosion"], 250),
                                                   self.bosses[current_boss].x, self.bosses[current_boss].y])
                self.enemy_explode_sfx.play()
                self.bosses[current_boss] = True
                current_boss += 1
                self.boss_time = False
                self.show_last_boss_bar = True
                self.player1.killed_boss = True
                self.switch_level = True
                update_wave()
                self.boss_label = Label("BOSS num. " + str(level), boss_label_xy[0], boss_label_xy[1],
                                        (255, 255, 0), boss_font_size, FONT, 'center', boss_label_xy)
                self.new_set_label.update("LEVEL " + str(level) + ": Wave " + str(wave) + " of 3", (255, 255, 0))

            # pickup update
            for count in range(level):
                self.pickups[count].update()

            for const_pickup in self.constant_pickups:
                const_pickup.update()

            # enemy update
            for enemy in self.enemies:
                enemy.update(self.player1.bullets, self.enemies, True)

            # enemy health checker
            for enemy in self.enemies:
                if enemy.helth <= 0:
                    self.enemy_explode_sfx.play()
                    tmp = enemy
                    self.killed_hidden.append(True)
                    self.killed_animations.append([Animation(self.sprites["explosion"], 200), enemy.x, enemy.y])
                    # print(self.killed_hidden)
                    self.enemies.remove(enemy)
                    if tmp.hit_by_player_num == 1:
                        self.player1.points += tmp.worth

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        for count in range(level):
            self.pickups[count].show(window)

        for const_pickup in self.constant_pickups:
            const_pickup.show(window)

        self.player1.show(window)

        global current_boss
        global player1_name

        if not self.show_boss_label and self.boss_time and self.bosses[current_boss].helth > 0:
            self.bosses[current_boss].show(window)
        for boss_killed_an, an_x, an_y in self.boss_killed_animation:
            boss_killed_an.animate(window, an_x, an_y, False, False)
            if self.show_last_boss_bar:
                window.screen.blit(self.sprites["boss-bar"].frames[5], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))


        for enemy in self.enemies:
            if enemy.y + image_size < HEIGHT:
                enemy.show(window)
            else:
                if len(self.killed_hidden) <= self.enemies_num:
                    self.killed_hidden.append(False)
                    # print(self.killed_hidden)

        for killed_animation, an_x, an_y in self.killed_animations:
            killed_animation.animate(window, an_x, an_y, False, False)

        if len(self.enemies) != 0 and self.player1.health <= 0:
            # self.sprites["death"].show_frames(window, (WIDTH / 2 - (self.death_img_size / 2), HEIGHT / 2 - (self.death_img_size / 2)))
            self.game_over = True
        if (type(self.bosses[len(self.bosses) - 1]) == bool and self.bosses[len(self.bosses) - 1]) and get_points_percent(self.max_points, self.player1.points) >= 70:
            self.win = True
        elif (type(self.bosses[len(self.bosses) - 1]) == bool and self.bosses[len(self.bosses) - 1]) and get_points_percent(self.max_points, self.player1.points) < 70:
            self.game_over = True
        if len(self.killed_hidden) >= self.enemies_num:
            if not self.switch_level:
                self.last_update = pygame.time.get_ticks()
                self.switch_level = True

                if wave == 3:
                    self.last_update = pygame.time.get_ticks()
                    self.boss_time = True
                    self.show_boss_label = True

                else:
                    update_wave()
                    self.new_set_label.update("LEVEL " + str(level) + ": Wave " + str(wave) + " of 3", (255, 255, 0))
            # self.sprites["win"].show_frames(window, (WIDTH / 2 - (self.win_img_size / 2), HEIGHT / 2 - (self.win_img_size / 2)))


        # Player 1 GUI
        self.p1_title_label.show(window)
        # self.p1_points_label.show(window)

        if self.switch_level and not self.boss_time:
            self.new_set_label.show(window)

        if self.show_boss_label:
            self.boss_label.show(window)

        if self.pause:
            self.pause_label.show(window)


"""""""""""""""""""""""""""
    MULTIPLAYER GAME SCENE
"""""""""""""""""""""""""""

class Multiplayer(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)
        self.max_points = create_random_levels()

        global level
        global wave
        level = 1
        wave = 1

        global joysticks
        self.heart_img_size = FRAME_OFFSET * self.sprites["heart"].scale
        self.death_img_size = FRAME_OFFSET * self.sprites["death"].scale
        self.win_img_size = FRAME_OFFSET * self.sprites["win"].scale

        self.boom_animation = Animation(self.sprites["explosion"], 200)

        self.enemy_bullets = [
            self.sprites["enemy_bullet"],
            self.sprites["enemy-purple-bullet"],
            self.sprites["enemy-blue-bullet"],
            self.sprites["enemy-yellow-bullet"]
        ]

        self.player_bullets = [
            self.sprites["player-purple-bullet"],
            self.sprites["player-blue-bullet"],
            self.sprites["player-yellow-bullet"],
            self.sprites["player-green-bullet"],
            self.sprites["player_bullet"]
        ]

        global player1_name
        global player2_name
        self.p1_title_label = Label(player1_name, self.heart_img_size - 40, 15, PLAYER1_COLOR, 40, FONT)
        self.p1_points_label = Label(str(0), self.heart_img_size, 80, TITANIUM_HWHITE, 40, FONT,
                                     'topleft',
                                     (self.heart_img_size, 80))
        self.p2_title_label = Label(player2_name, WIDTH - self.heart_img_size - 110, 15, PLAYER2_COLOR, 40, FONT)
        self.p2_points_label = Label(str(0), WIDTH - self.heart_img_size, 80,
                                     TITANIUM_HWHITE, 40, FONT, 'topright', (WIDTH - self.heart_img_size, 80))

        self.player1 = Player(self.p1_points_label, self.sprites["dash-left-right"], self.sprites["dash-up-down"], self.sprites["explosion"], self.sprites["fuel-fire"], self.sprites["heart"], self.sprites["player1"],
                              image_size, HEIGHT-image_size, self.sprites["player_bullet"],
                              1, list(joysticks), player1_joyid)
        self.player2 = Player(self.p2_points_label, self.sprites["dash-left-right"], self.sprites["dash-up-down"],
                              self.sprites["explosion"], self.sprites["fuel-fire"], self.sprites["heart"],
                              self.sprites["player2"],
                              image_size + image_size, HEIGHT - image_size, self.sprites["player_bullet"],
                              2, list(joysticks), player2_joyid)
        self.player1.set_controls(player1_controls)
        self.player2.set_controls(player2_controls)

        self.enemies = read_enemies(lvl_file, self.sprites["enemies"], self.sprites["explosion"], self.enemy_bullets, 150, 80)
        self.pressed_keys = None

        self.enemy_explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)
        self.hidden = 0

        self.killed_hidden = []  # [None] * len(self.enemies)
        self.killed_animations = []
        self.boss_killed_animation = []
        self.timer_level = 0
        self.last_update = pygame.time.get_ticks()
        self.timer = 0
        self.cooldown = 100

        self.switch_level = False
        self.new_set_label = new_lw_label
        self.boss_label = boss_label
        self.enemies_num = len(self.enemies)

        self.bosses = [
            FirstBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["first-boss"], WIDTH / 2,
                      HEIGHT / 4, self.enemy_bullets[0], 70.0),
            SecondBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["second-boss"], WIDTH / 2,
                       HEIGHT / 4, self.enemy_bullets[1], 65.0),
            ThirdBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["third-boss"], WIDTH / 2,
                      HEIGHT / 4, self.enemy_bullets[2], 55.0),
            FourthBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["fourth-boss"], WIDTH / 2,
                       HEIGHT / 4, self.enemy_bullets[3], 50.0),
            FinalBoss(self.sprites["explosion"], self.sprites["boss-bar"], self.sprites["final-boss"], WIDTH / 2,
                      HEIGHT / 4, self.enemy_bullets[1], 45.0),
        ]

        self.pickups = [
            Pickup(self.sprites["green-pickup"], 5.0, 1.5, 0, "green", self.player_bullets[3], 2),
            Pickup(self.sprites["purple-pickup"], 3.0, 2.0, 0, "purple", self.player_bullets[0], 3),
            Pickup(self.sprites["blue-pickup"], 10.0, 3.0, 0, "blue", self.player_bullets[1], 4),
            Pickup(self.sprites["yellow-pickup"], 8.0, 2.5, 0, "yellow", self.player_bullets[2], 5),
            Pickup(self.sprites["red-pickup"], 8.0, 2.5, 0, "red", self.player_bullets[4], 1),
        ]

        self.constant_pickups = [
            Pickup(self.sprites["red-pickup"], 8.0, 2.5, 0, "red", self.player_bullets[4], 1),
            Pickup(self.sprites["heal-pickup"], 9.0, 3.5, 3, "heal", None)
        ]

        self.boss_time = False
        self.show_boss_label = False
        self.show_last_boss_bar = False
        self.killed_boss = False
        self.pause = False
        self.pause_label = pause_label
        self.game_over = False
        self.win = False

    def process_input(self, events, pressed_keys):
        global current_boss

        self.pressed_keys = pressed_keys
        for event in events:
            if not self.pause:
                if self.player1.health > 0:
                    self.player1.event_handler(event)
                if self.player2.health > 0:
                    self.player2.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    self.pause = not self.pause

        if self.game_over:
            save_points(POINTS, [[self.player1, player1_name], [self.player2, player2_name]])
            self.switch_to_scene(DeathScene(self.sprites))

        if self.win:
            save_points(POINTS, [[self.player1, player1_name], [self.player2, player2_name]])
            self.switch_to_scene(WinScene(self.sprites))

    def update(self):
        if not self.pause:
            global current_boss

            current_time = pygame.time.get_ticks()
            if self.switch_level:
                if current_time - self.last_update >= self.cooldown:
                    self.timer += 1
                    self.last_update = current_time
                    if self.timer >= self.cooldown:
                        if self.boss_time:
                            self.timer = 0
                            # print("BOSS")
                            self.show_boss_label = False

                        else:
                            self.enemies = read_enemies(lvl_file, self.sprites["enemies"], self.sprites["explosion"], self.enemy_bullets, 150, 80)
                            self.show_last_boss_bar = False
                            self.killed_hidden = []
                            self.killed_animations = []
                            self.boss_killed_animation = []
                            self.enemies_num = len(self.enemies)
                            # print("NEXT LEVEL !!")
                            self.timer = 0
                            self.switch_level = False

            en_bullets = []
            for enemy in self.enemies:
                en_bullets += enemy.en_bullets

            if not self.show_boss_label and self.boss_time:
                en_bullets += self.bosses[current_boss].en_bullets

            self.player1.update(self.pressed_keys, en_bullets, self.pickups + self.constant_pickups)
            self.player2.update(self.pressed_keys, en_bullets, self.pickups + self.constant_pickups)
            # self.p1_points_label.update(str(self.player1.points), TITANIUM_HWHITE)

            # boss update
            if not self.show_boss_label and self.boss_time:
                self.bosses[current_boss].update(self.player1.bullets + self.player2.bullets)

            if self.bosses[current_boss].helth <= 0:
                # self.bosses[0].defeated = True
                self.last_update = pygame.time.get_ticks()
                self.boss_killed_animation.append([Animation(self.sprites["boss-explosion"], 250),
                                                   self.bosses[current_boss].x, self.bosses[current_boss].y])
                self.enemy_explode_sfx.play()
                self.bosses[current_boss] = True
                current_boss += 1
                self.boss_time = False
                self.show_last_boss_bar = True

                self.player1.killed_boss = True
                self.player2.killed_boss = True

                self.switch_level = True
                update_wave()
                self.boss_label = Label("BOSS num. " + str(level), boss_label_xy[0], boss_label_xy[1],
                                        (255, 255, 0), boss_font_size, FONT, 'center', boss_label_xy)
                self.new_set_label.update("LEVEL " + str(level) + ": Wave " + str(wave) + " of 3", (255, 255, 0))

            # pickup update
            for count in range(level):
                self.pickups[count].update()

            for const_pickup in self.constant_pickups:
                const_pickup.update()

            # enemy update
            for enemy in self.enemies:
                enemy.update(self.player1.bullets + self.player2.bullets, self.enemies, True)

            # enemy health checker
            for enemy in self.enemies:
                if enemy.helth <= 0:
                    self.enemy_explode_sfx.play()
                    tmp = enemy
                    self.killed_hidden.append(True)
                    self.killed_animations.append([Animation(self.sprites["explosion"], 200), enemy.x, enemy.y])
                    # print(self.killed_hidden)
                    self.enemies.remove(enemy)
                    if tmp.hit_by_player_num == 1:
                        self.player1.points += tmp.worth
                    elif tmp.hit_by_player_num == 2:
                        self.player2.points += tmp.worth

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        for count in range(level):
            self.pickups[count].show(window)

        for const_pickup in self.constant_pickups:
            const_pickup.show(window)

        self.player1.show(window)
        self.player2.show(window)

        global current_boss
        global player1_name
        global player2_name

        if not self.show_boss_label and self.boss_time and self.bosses[current_boss].helth > 0:
            self.bosses[current_boss].show(window)
        for boss_killed_an, an_x, an_y in self.boss_killed_animation:
            boss_killed_an.animate(window, an_x, an_y, False, False)
            if self.show_last_boss_bar:
                window.screen.blit(self.sprites["boss-bar"].frames[5], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))


        for enemy in self.enemies:
            if enemy.y + image_size < HEIGHT:
                enemy.show(window)
            else:
                if len(self.killed_hidden) <= self.enemies_num:
                    self.killed_hidden.append(False)
                    # print(self.killed_hidden)

        for killed_animation, an_x, an_y in self.killed_animations:
            killed_animation.animate(window, an_x, an_y, False, False)

        if len(self.enemies) != 0 and self.player1.health <= 0 and self.player2.health <= 0:
            # self.sprites["death"].show_frames(window, (WIDTH / 2 - (self.death_img_size / 2), HEIGHT / 2 - (self.death_img_size / 2)))
            self.game_over = True
        if (type(self.bosses[len(self.bosses) - 1]) == bool and self.bosses[len(self.bosses) - 1]) and (get_points_percent(self.max_points, self.player1.points + self.player2.points) >= 70):
            self.win = True
        elif (type(self.bosses[len(self.bosses) - 1]) == bool and self.bosses[len(self.bosses) - 1]) and (get_points_percent(self.max_points, self.player1.points + self.player2.points) < 70):
            self.game_over = True

        if len(self.killed_hidden) >= self.enemies_num:
            if not self.switch_level:
                self.last_update = pygame.time.get_ticks()
                self.switch_level = True

                if wave == 3:
                    self.last_update = pygame.time.get_ticks()
                    self.boss_time = True
                    self.show_boss_label = True

                else:
                    update_wave()
                    self.new_set_label.update("LEVEL " + str(level) + ": Wave " + str(wave) + " of 3", (255, 255, 0))

            # self.sprites["win"].show_frames(window, (WIDTH / 2 - (self.win_img_size / 2), HEIGHT / 2 - (self.win_img_size / 2)))


        # Player 1 GUI
        self.p1_title_label.show(window)
        # Player 2 GUI
        self.p2_title_label.show(window)

        # self.p1_points_label.show(window)

        if self.switch_level and not self.boss_time:
            self.new_set_label.show(window)

        if self.show_boss_label:
            self.boss_label.show(window)

        if self.pause:
            self.pause_label.show(window)


class DeathScene(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        self.explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)
        self.explosion_animation = Animation(self.sprites["explosion"], 500)

        self.explosions = []
        self.create_explosions(100)

        self.planet = pygame.image.load(PLANET)

        self.death_label = death_label

    def create_explosions(self, num):
        for exps in range(num):
            exp_x = random.randint(0, WIDTH)
            exp_y = random.randint(0, HEIGHT)
            cooldown = random.randint(100, 1000)
            self.explosions.append([Animation(self.sprites["explosion"], cooldown), exp_x, exp_y])

    def process_input(self, events, pressed_keys):
        global is_multiplayer

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_slow_stars(window)

        window.screen.blit(self.planet, (0, 0))

        for exp, exp_x, exp_y in self.explosions:
            exp.animate(window, exp_x, exp_y, True, False, self.explode_sfx)

        self.death_label.show(window)


class WinScene(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        self.explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)
        self.explosion_animation = Animation(self.sprites["explosion"], 500)
        self.planet = pygame.image.load(PLANET)

        self.win_label = win_label

    def process_input(self, events, pressed_keys):
        global is_multiplayer

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.switch_to_scene(TitleScene(self.sprites))

    def update(self):
        pass

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_slow_stars(window)

        window.screen.blit(self.planet, (0, 0))
        self.win_label.show(window)



class Multiplayer2(Scene):
    def __init__(self, sprites):
        super().__init__(sprites)

        # self.player1 = Player(self.sprites["heart"], self.sprites["player1"],
        #                       image_size, HEIGHT-image_size, self.sprites["player_bullet"],
        #                       joysticks, 1, 1)

        global joysticks
        self.heart_img_size = FRAME_OFFSET * self.sprites["heart"].scale
        self.death_img_size = FRAME_OFFSET * self.sprites["death"].scale
        self.win_img_size = FRAME_OFFSET * self.sprites["win"].scale

        self.player1 = Player(self.sprites["heart"], self.sprites["player1"],
                              image_size, HEIGHT - image_size, self.sprites["player_bullet"],
                              1, list(joysticks), player1_joyid)

        self.player2 = Player(self.sprites["heart"], self.sprites["player2"],
                              image_size + image_size, HEIGHT - image_size, self.sprites["player_bullet"],
                              2, list(joysticks), player2_joyid)

        self.player2.set_controls({
            "up": pygame.K_w,
            "down": pygame.K_s,
            "left": pygame.K_a,
            "right": pygame.K_d,
            "fire": pygame.K_k
        })

        global player1_name
        global player2_name
        self.p1_title_label = Label(player1_name, self.heart_img_size - 40, 15, PLAYER1_COLOR, 40, FONT)
        self.p1_points_label = Label(str(self.player1.points), self.heart_img_size, 80, TITANIUM_HWHITE, 40, FONT,
                                     'topleft',
                                     (self.heart_img_size, 80))

        self.p2_title_label = Label(player2_name, WIDTH - self.heart_img_size - 110, 15, PLAYER2_COLOR, 40, FONT)
        self.p2_points_label = Label("{p2}".format(p2=self.player2.points), WIDTH - self.heart_img_size, 80, TITANIUM_HWHITE, 40, FONT, 'topright', (WIDTH - self.heart_img_size, 80))

        self.enemies = read_enemies("test0_0.ens", self.sprites["enemies"], self.sprites["enemy_bullet"], 150, 80)
        self.pressed_keys = None

        self.enemy_explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)

    def process_input(self, events, pressed_keys):
        self.pressed_keys = pressed_keys
        for event in events:
            if self.player1.health > 0:
                self.player1.event_handler(event)
            if self.player2.health > 0:
                self.player2.event_handler(event)

    def update(self):
        en_bullets = []
        for enemy in self.enemies:
            en_bullets += enemy.en_bullets

        self.player1.update(self.pressed_keys, en_bullets)
        self.player2.update(self.pressed_keys, en_bullets)

        self.p1_points_label.update(str(self.player1.points), TITANIUM_HWHITE)
        self.p2_points_label.update(str(self.player2.points), TITANIUM_HWHITE)

        # enemy update
        for enemy in self.enemies:
            enemy.update(self.player1.bullets + self.player2.bullets, self.enemies, True)

        # enemy health checker
        for enemy in self.enemies:
            if enemy.helth <= 0:
                self.enemy_explode_sfx.play()
                tmp = enemys
                self.enemies.remove(enemy)
                if tmp.hit_by_player_num == 1:
                    self.player1.points += tmp.worth
                elif tmp.hit_by_player_num == 2:
                    self.player2.points += tmp.worth

    def show(self, window: Window):
        window.screen.fill(BLACK)
        animate_stars(window)

        self.player1.show(window)
        self.player2.show(window)

        for enemy in self.enemies:
            enemy.show(window)

        if len(self.enemies) != 0 and self.player1.health <= 0 and self.player2.health <= 0:
            self.sprites["death"].show_frames(window, (WIDTH / 2 - (self.death_img_size / 2), HEIGHT / 2 - (self.death_img_size / 2)))
        if len(self.enemies) == 0:
            self.sprites["win"].show_frames(window, (WIDTH / 2 - (self.win_img_size / 2), HEIGHT / 2 - (self.win_img_size / 2)))

        # Player 1 GUI
        self.p1_title_label.show(window)
        self.p1_points_label.show(window)

        # Player 2 GUI
        self.p2_title_label.show(window)
        self.p2_points_label.show(window)

