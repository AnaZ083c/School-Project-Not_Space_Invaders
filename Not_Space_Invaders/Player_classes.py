from Sprite import Sprite, Animation
from constants_and_globals import *
from Enemy_classes import Enemy, Enemies
from Window import Window
import pygame


class Player:
    def __init__(self, player_hearts: Sprite, player_sprites: Sprite, x, y, bullet_sprites: Sprite, player_num: int = 1, joysticks: list = None, joystick_index: int = -1):  # keyboard_controls = [ up, down, left, right ]
        self.player_sprites = player_sprites
        self.player_hearts = player_hearts
        self.player_num = player_num

        self.hearts_xys = []

        self.x = x
        self.y = y
        self.health = 5

        self.bullet_sprites = bullet_sprites
        self.bullet_x = self.x
        self.bullet_y = self.y
        self.bullet = Bullet(bullet_sprites, self, self.bullet_x, self.bullet_y)

        self.bullets = []
        self.bullet_shot = True
        self.points = 0

        self.frame = 0  # idle
        self.move_speed = 5
        self.original_speed = self.move_speed
        self.bullet_speed = 10
        self.is_moving = False
        self.keyboard_controls = {"up": pygame.K_UP,
                                  "down": pygame.K_DOWN,
                                  "left": pygame.K_LEFT,
                                  "right": pygame.K_RIGHT,
                                  "fire": pygame.K_KP_ENTER}
        self.joystick_index = joystick_index
        self.joysticks = joysticks
        self.motion = [0, 0]
        self.shooting = False

        self.bullet_cooldown = 0
        self.speedup = False

        self.get_hearts_xys()

        self.sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.current_hit_sfx = 0
        self.hit_sfx = pygame.mixer.Sound(player_hit_sfxs[self.current_hit_sfx])
        self.explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)

    # moving and stuff
    def update(self, keys: pygame.key, bullet_list):
        if self.health > 0:
            if sum(keys) >= 1:  # preveri ali je bila sploh kakšna tipka pritisnjena in, če ja, pogleda, če je bila to katera izmed kontrol za playerja
                if keys[self.keyboard_controls.get("up")]:
                    self.is_moving = True
                    self.y -= self.move_speed
                    self.frame = 0
                if keys[self.keyboard_controls.get("down")]:
                    self.is_moving = True
                    self.y += self.move_speed
                    self.frame = 0
                if keys[self.keyboard_controls.get("left")]:
                    self.is_moving = True
                    self.x -= self.move_speed
                    self.frame = 1
                if keys[self.keyboard_controls.get("right")]:
                    self.is_moving = True
                    self.x += self.move_speed
                    self.frame = 2
            else:
                self.bullet_shot = True
                self.is_moving = False
                self.frame = 0
            if not (self.joystick_index == -1):
                if self.joysticks[self.joystick_index] is not None:
                    if abs(self.motion[0]) < 0.3:
                        self.motion[0] = 0
                        self.frame = 0
                    if abs(self.motion[1]) < 0.3:
                        self.motion[1] = 0
                        self.frame = 0

                    if self.motion[0] < 0:
                        self.frame = 1
                    if self.motion[0] > 0:
                        self.frame = 2

                    self.x += self.motion[0] * self.move_speed
                    self.y += self.motion[1] * self.move_speed

                    if self.speedup:
                        self.move_speed *= 20
                        self.speedup = False
                    else:
                        self.move_speed = self.original_speed
            self.out_of_bounds_handler()
            self.bullet_collision_handler(bullet_list)

    def event_handler(self, event: pygame.event):
        # print(self.shooting)
        if event.type == pygame.JOYBUTTONDOWN:
            if event.joy == self.joysticks[self.joystick_index][1]:
                # print(event.button)
                if event.button == 0:
                    self.shooting = True
                    self.sfx.play()
                    self.bullets.append(Bullet(self.bullet_sprites, self, self.x, self.y))
                if event.button == 5:
                    self.speedup = True
        if event.type == pygame.JOYBUTTONUP:
            if event.joy == self.joysticks[self.joystick_index][1]:
                if event.button == 0:
                    self.shooting = False
        if event.type == pygame.JOYAXISMOTION:
            if event.joy == self.joysticks[self.joystick_index][1]:
                # print(event.axis)
                if event.axis < 2:
                    self.motion[event.axis] = event.value

        if event.type == pygame.JOYHATMOTION:
            if event.joy == self.joysticks[self.joystick_index][1]:
                pass
        # if self.shooting:
        #     if self.bullet_cooldown <= 0:
        #         self.bullet_cooldown = 2
        #         self.bullets.append(Bullet(self.bullet_sprites, self, self.x, self.y))
        #     else:
        #         self.bullet_cooldown -= 1
        if event.type == pygame.KEYDOWN:
            if event.key == self.keyboard_controls.get("fire"):
                self.sfx.play()
                self.bullets.append(Bullet(self.bullet_sprites, self, self.x, self.y))

    # change moving speed
    def set_move_speed(self, new_move_speed):
        self.move_speed = new_move_speed
        self.original_speed = self.move_speed

    # change keys
    def set_controls(self, new_controls: dict):
        self.keyboard_controls = new_controls

    def set_joystick(self, new_joystick_index):
        self.joystick_index = new_joystick_index

    def out_of_bounds_handler(self):
        if self.x + image_size > WIDTH:
            self.x = WIDTH - image_size
        if self.x < 0:
            self.x = 0
        if self.y + image_size >= HEIGHT:
            self.y = HEIGHT - image_size
        if self.y < 0:
            self.y = 0

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + 50) and (self.y - 60 <= bullet.y <= self.y + 60):
                self.hit_sfx.play()
                # print('x, y =', bullet.x, bullet.y)
                bullet.hit = True
                self.health -= 1
                if self.health <= 0:
                    self.explode_sfx.play()
                # print('player', self.health)

                if self.current_hit_sfx < len(player_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(player_hit_sfxs[self.current_hit_sfx])
            else:
                continue
                # bullet.hit = False

    def show(self, window: Window):
        if self.health > 0:
            for bullet in self.bullets:
                bullet.collision_handler()
                bullet.show(window, self.bullet_speed)
                if bullet.y <= 0 or bullet.hit:
                    self.bullets.remove(bullet)
            window.screen.blit(self.player_sprites.frames[self.frame], (self.x, self.y))
            for i in range(0, self.health):
                window.screen.blit(self.player_hearts.frames[0], self.hearts_xys[i])

    def get_hearts_xys(self):
        hearts_img_size = FRAME_OFFSET * self.player_hearts.scale
        for i in range(0, self.health):
            if self.player_num == 1:
                self.hearts_xys.append((i * hearts_img_size, 40))
            elif self.player_num == 2:
                self.hearts_xys.append((WIDTH-(hearts_img_size*i)-50, 40))


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Bullet:
    def __init__(self, bullet_sprites: Sprite, owner: object, x, y):
        self.owner = owner
        self.bullet_sprites = bullet_sprites
        self.x = x
        self.y = y
        self.animation = Animation(bullet_sprites, 10)
        self.hit = False
        self.frame = 2

    def collision_handler(self):
        # print("bullet ", self.hit)
        if self.hit:
            self.frame = 0

    def bullet_update(self):
        self.collision_handler()

    def show(self, window: Window, bullet_speed, down_to_up: bool = True):
        self.animation.update(window, self.x, self.y, False)
        if down_to_up:
            if self.y > 0:
                self.y -= bullet_speed
                window.screen.blit(self.bullet_sprites.frames[self.frame], (self.x, self.y))
        else:
            if self.y < HEIGHT:
                self.y += bullet_speed
                window.screen.blit(self.bullet_sprites.frames[self.frame], (self.x, self.y))
