from Sprite import Sprite, Animation
from constants_and_globals import *
from Enemy_classes import Enemy, Enemies
from Label import Label
from Window import Window
import pygame


class Player:
    def __init__(self, points_label: Label, dash_left_right: Sprite, dash_up_down: Sprite, boom: Sprite, fuel_fire: Sprite, player_hearts: Sprite, player_sprites: Sprite, x, y, bullet_sprites: Sprite, player_num: int = 1, joysticks: list = None, joystick_index: int = -1, health: int = 5, points: int = 0):  # keyboard_controls = [ up, down, left, right ]
        self.player_sprites = player_sprites
        self.player_hearts = player_hearts
        self.dash_left_right = dash_left_right
        self.dash_up_down = dash_up_down
        self.fuel_fire_sprite = fuel_fire
        self.fuel_fire_animation = Animation(fuel_fire, 100)
        self.boom_sprite = boom
        self.boom_animation = Animation(boom, 200)
        self.player_num = player_num

        self.dash_left_right_frame = 0  # left
        self.dash_up_down_frame = 0  # up
        self.hearts_xys = []

        self.points_label = points_label

        self.x = x
        self.y = y
        self.health = health
        self.max_health = self.health
        self.healed = False
        self.draw_speedup = False

        self.fuel_fire_x = self.x

        self.bullet_sprites = bullet_sprites
        self.bullet_dmg_give = 1
        self.bullet_x = self.x
        self.bullet_y = self.y
        self.bullet = Bullet(bullet_sprites, self, self.bullet_x, self.bullet_y, self.bullet_dmg_give)

        self.bullets = []
        self.bullet_shot = True
        self.points = points

        self.frame = 0  # idle
        self.move_speed = 5
        self.original_speed = self.move_speed
        self.bullet_speed = 10
        self.is_moving = False
        self.keyboard_controls = {"up": pygame.K_UP,
                                  "down": pygame.K_DOWN,
                                  "left": pygame.K_LEFT,
                                  "right": pygame.K_RIGHT,
                                  "fire": pygame.K_KP_ENTER,
                                  "dash": pygame.K_KP3}
        self.joystick_index = joystick_index
        self.joysticks = joysticks
        self.motion = [0, 0]
        self.shooting = False

        self.bullet_cooldown = 0
        self.speedup = False

        self.draw_speedup_up_down = False
        self.draw_speedup_left_right = False
        self.last_speedup = None
        self.timer = 0
        self.speedup_cooldown = 5

        self.shoot_timer = 0
        self.shoot_cooldown = 20
        self.last_shoot = pygame.time.get_ticks()
        self.is_enter_down = False

        self.get_hearts_xys()

        self.last_heart_y = 40

        self.sfx = pygame.mixer.Sound(PLAYER_RED_BULLET_SFX)
        self.current_hit_sfx = 0
        self.hit_sfx = pygame.mixer.Sound(player_hit_sfxs[self.current_hit_sfx])
        self.explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)

        self.killed_boss = False

    # moving and stuff
    def update(self, keys: pygame.key, bullet_list, pickup_list):
        if self.health > 0:
            current_time = pygame.time.get_ticks()
            if self.last_speedup is not None:
                if current_time - self.last_speedup >= self.speedup_cooldown:  # if 10 ms have passed, move on to the next frame
                    self.timer += 1
                    self.last_speedup = current_time
                    if self.timer >= self.speedup_cooldown:
                        self.draw_speedup_left_right = False
                        self.draw_speedup_up_down = False
                        self.draw_speedup = False
                        self.last_speedup = None
                        self.timer = 0

            if self.is_enter_down and self.shoot_timer <= 0:
                self.shoot()
                self.shoot_timer = self.shoot_cooldown
            else:
                self.shoot_timer -= 1



            if sum(keys) >= 1:  # preveri ali je bila sploh kakšna tipka pritisnjena in, če ja, pogleda, če je bila to katera izmed kontrol za playerja
                if keys[self.keyboard_controls.get("up")]:
                    self.is_moving = True
                    self.y -= self.move_speed
                    self.frame = 0
                    self.dash_up_down_frame = 0
                    self.draw_speedup_up_down = True
                    self.draw_speedup_left_right = False
                if keys[self.keyboard_controls.get("down")]:
                    self.is_moving = True
                    self.y += self.move_speed
                    self.frame = 0
                    self.dash_up_down_frame = 1
                    self.draw_speedup_up_down = True
                    self.draw_speedup_left_right = False
                if keys[self.keyboard_controls.get("left")]:
                    self.is_moving = True
                    self.x -= self.move_speed
                    self.frame = 1
                    self.dash_left_right_frame = 0
                    self.draw_speedup_up_down = False
                    self.draw_speedup_left_right = True
                if keys[self.keyboard_controls.get("right")]:
                    self.is_moving = True
                    self.x += self.move_speed
                    self.frame = 2
                    self.dash_left_right_frame = 1
                    self.draw_speedup_up_down = False
                    self.draw_speedup_left_right = True
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

                    if self.motion[1] > 0:
                        self.dash_up_down_frame = 1
                        self.draw_speedup_up_down = True
                        self.draw_speedup_left_right = False
                    if self.motion[1] < 0:
                        self.dash_up_down_frame = 0
                        self.draw_speedup_up_down = True
                        self.draw_speedup_left_right = False
                    if self.motion[0] < 0:
                        self.frame = 1
                        self.dash_left_right_frame = 0
                        self.draw_speedup_up_down = False
                        self.draw_speedup_left_right = True
                    if self.motion[0] > 0:
                        self.frame = 2
                        self.dash_left_right_frame = 1
                        self.draw_speedup_up_down = False
                        self.draw_speedup_left_right = True

                    self.x += self.motion[0] * self.move_speed
                    self.y += self.motion[1] * self.move_speed

            if self.speedup:
                self.move_speed *= 20
                self.draw_speedup = True
                self.last_speedup = pygame.time.get_ticks()
                self.speedup = False
            else:
                self.move_speed = self.original_speed
            self.out_of_bounds_handler()
            self.pickup_collision_handler(pickup_list)
            self.boss_reward_handler()
            self.bullet_collision_handler(bullet_list)
            self.points_label.update(str(self.points), TITANIUM_HWHITE)

    def boss_reward_handler(self):
        if self.killed_boss:
            self.update_health(2)
            self.killed_boss = False
            self.__init__(self.points_label, self.dash_left_right, self.dash_up_down, self.boom_sprite, self.fuel_fire_sprite, self.player_hearts, self.player_sprites, self.x, self.y, self.bullet_sprites, self.player_num, self.joysticks, self.joystick_index, self.max_health, self.points)
            if self.player_num == 2:
                self.set_controls({
                    "up": pygame.K_w,
                    "down": pygame.K_s,
                    "left": pygame.K_a,
                    "right": pygame.K_d,
                    "fire": pygame.K_k,
                    "dash": pygame.K_SPACE
                })

    def shoot(self):
        self.sfx.play()
        self.bullets.append(Bullet(self.bullet_sprites, self, self.x, self.y, self.bullet_dmg_give))

    def event_handler(self, event: pygame.event):
        # print(self.shooting)
        if self.joystick_index != -1:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.joy == self.joysticks[self.joystick_index][1]:
                    if event.button == 0:
                        self.is_enter_down = True
                        self.shoot()
                    if event.button == 5:
                        self.speedup = True
            if event.type == pygame.JOYBUTTONUP:
                if event.joy == self.joysticks[self.joystick_index][1]:
                    if event.button == 0:
                        self.is_enter_down = False
            if event.type == pygame.JOYAXISMOTION:
                if event.joy == self.joysticks[self.joystick_index][1]:
                    if event.axis < 2:
                        self.motion[event.axis] = event.value

            if event.type == pygame.JOYHATMOTION:
                if event.joy == self.joysticks[self.joystick_index][1]:
                    pass
        if event.type == pygame.KEYDOWN:
            if event.key == self.keyboard_controls.get("dash"):
                self.speedup = True
            if event.key == self.keyboard_controls.get("fire"):
                self.is_enter_down = True
                self.shoot()
        if event.type == pygame.KEYUP:
            if event.key == self.keyboard_controls.get("fire"):
                self.is_enter_down = False

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
                self.health -= bullet.dmg_give
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

    def pickup_collision_handler(self, pickup_list):
        for pickup in pickup_list:
            # pickup.collision_with_player(self)
            if (self.x - 50 <= pickup.x <= self.x + 50) and (self.y - 60 <= pickup.y <= self.y + 60):
                if not pickup.pickup:
                    pickup.pickup_sfx.play()
                pickup.pickup = True
                if pickup.name == "heal":
                    if self.health < self.max_health:
                        self.health += 1
                else:
                    self.bullet_sprites = pickup.bullet_sprite
                    self.bullet_dmg_give = pickup.dmg_give
                    self.shoot_cooldown = pickup.shoot_cooldown
                    # print("bullet dmg = ", self.bullet.dmg_give)
                pickup.last_spawn_time = pygame.time.get_ticks()
            else:
                continue

    def show(self, window: Window):
        if self.health > 0:
            for bullet in self.bullets:
                bullet.collision_handler()
                bullet.show(window, self.bullet_speed)
                if bullet.y <= 0 or bullet.hit:
                    self.bullets.remove(bullet)
            if self.draw_speedup:
                if self.draw_speedup_up_down:
                    if self.dash_up_down_frame == 0:
                        window.screen.blit(self.dash_up_down.frames[self.dash_up_down_frame], (self.x, self.y + image_size))
                    elif self.dash_up_down_frame == 1:
                        window.screen.blit(self.dash_up_down.frames[self.dash_up_down_frame], (self.x, self.y - image_size))
                elif self.draw_speedup_left_right:
                    if self.dash_left_right_frame == 0:
                        window.screen.blit(self.dash_left_right.frames[self.dash_left_right_frame], (self.x + image_size, self.y))
                    elif self.dash_left_right_frame == 1:
                        window.screen.blit(self.dash_left_right.frames[self.dash_left_right_frame], (self.x - image_size, self.y))
            window.screen.blit(self.player_sprites.frames[self.frame], (self.x, self.y))
            if self.frame == 0:
                self.fuel_fire_animation.animate(window, self.x, self.y + image_size/2.5)
            elif self.frame == 1:
                self.fuel_fire_animation.animate(window, self.x + 5, self.y + image_size/2.5)
            elif self.frame == 2:
                self.fuel_fire_animation.animate(window, self.x - 9, self.y + image_size / 2.5)
            for i in range(0, self.health):
                window.screen.blit(self.player_hearts.frames[0], self.hearts_xys[i])
        else:
            self.boom_animation.animate(window, self.x, self.y, False, False)

        self.points_label.show(window)

    def get_hearts_xys(self):
        hearts_img_size = FRAME_OFFSET * self.player_hearts.scale  # 28.8
        # print("HEARTS_IMG_SIZE", hearts_img_size)
        # print("HEALTH: ", self.health)
        # print("MAX HEALTH: ", self.health)
        heart_y = 80
        heart_x = 0
        heart_count = 0
        for i in range(0, self.health):
            if self.player_num == 1:
                if heart_count == 5:
                    heart_y += 40
                    heart_x = 0
                    heart_count = 0
                self.hearts_xys.append((heart_x * hearts_img_size, heart_y))
                heart_x += 1
                heart_count += 1
            elif self.player_num == 2:
                if heart_count == 5:
                    heart_y += 40
                    heart_x = 0
                    heart_count = 0
                self.hearts_xys.append((WIDTH - (heart_x * hearts_img_size) - 50, heart_y))
                heart_x += 1
                heart_count += 1
        self.last_heart_y = heart_y
        # self.points_label.change_y(heart_y + hearts_img_size)

    def update_health(self, factor):
        self.max_health += factor
        self.health = self.max_health
        self.get_hearts_xys()


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Bullet:
    def __init__(self, bullet_sprites: Sprite, owner: object, x, y, dmg_give: int = 1):
        self.owner = owner
        self.bullet_sprites = bullet_sprites
        self.x = x
        self.y = y
        self.animation = Animation(bullet_sprites, 10)
        self.hit = False
        self.frame = len(self.bullet_sprites.frames) - 1  # 2
        self.name = "bullet"
        self.dmg_give = dmg_give

    def change_dmg(self, new_dmg):
        self.dmg_give = new_dmg

    def change_sprites(self, new_sprites):
        self.bullet_sprites = new_sprites

    def collision_handler(self):
        # print("bullet ", self.hit)
        if self.hit:
            self.frame = 0

    def bullet_update(self):
        self.collision_handler()

    def show(self, window: Window, bullet_speed, down_to_up: bool = True):
        self.animation.animate(window, self.x, self.y, False)
        if down_to_up:
            if self.y > 0:
                self.y -= bullet_speed
                window.screen.blit(self.bullet_sprites.frames[self.frame], (self.x, self.y))
        else:
            if self.y < HEIGHT:
                self.y += bullet_speed
                window.screen.blit(self.bullet_sprites.frames[self.frame], (self.x, self.y))
