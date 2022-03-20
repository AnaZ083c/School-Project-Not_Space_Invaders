import random

from Sprite import Sprite, Animation
import Player_classes as pc
from constants_and_globals import *
from Window import Window
import pygame


class Enemy:
    def __init__(self, boom: Sprite, enemy_sprites: Sprite, x, y, bullet_sprites: Sprite, shoot_cooldown: float = 40.0, worth: int = 3, dmg_give: int = 1, max_helth: int = 3):  # keyboard_controls = [ up, down, left, right ]
        self.enemy_sprites = enemy_sprites
        self.enemy_animation = Animation(enemy_sprites, 400)
        self.dmg_give = dmg_give

        self.helth = max_helth
        self.max_helth = max_helth

        self.was_hit = False
        self.worth = worth
        self.hit_by_player_num = 0
        self.dmg_taken = 1
        self.boom_animation = Animation(boom, 100)

        self.x = x
        self.y = y

        self.en_bullet_x = self.x
        self.en_bullet_y = self.y
        self.en_bullets = []
        self.en_bullet_shot = True

        self.bullet_sprites = bullet_sprites
        self.en_bullet_x = self.x
        self.en_bullet_y = self.y
        self.en_bullet = pc.Bullet(bullet_sprites, self, self.en_bullet_x, self.en_bullet_y, self.dmg_give)

        self.move_speed = 2
        self.bullet_speed = 2.5
        self.is_moving = False

        self.last_update = pygame.time.get_ticks()
        self.shoot_cooldown = shoot_cooldown
        self.timer = 0
        self.direction = 1

        self.sfx = pygame.mixer.Sound(GENERIC_ENEMY_BULLET_SFX)

        self.current_hit_sfx = 0
        self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
        self.explode_sfx = pygame.mixer.Sound(ENEMY_EXPLODE)

        self.moving_down = False
        self.animate_boom = False

        # self.showing = True

    # moving and stuff
    def update(self, bullet_list, enemies, is_group: bool = False):
        current_time = pygame.time.get_ticks()
        if self.y + image_size < HEIGHT:
            if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
                self.timer += 1
                self.last_update = current_time
                if self.timer >= self.shoot_cooldown:
                    # play shoot sfx
                    self.sfx.play()
                    # shoot
                    self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y, self.dmg_give))
                    self.timer = 0
        # else:
        #    self.showing = False

        self.x += (self.move_speed * self.direction)
        if self.helth <= 0:
            self.animate_boom = True

        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler(enemies, is_group)

    # change moving speed
    def set_move_speed(self, new_move_speed):
        self.move_speed = new_move_speed

    def out_of_bounds_handler(self, enemies: list, is_group: bool):
        if not is_group:
            if self.x + image_size > WIDTH:
                self.x = WIDTH - image_size
                self.y += self.enemy_sprites.img_size/4
                self.direction = -1
            if self.x < 0:
                self.x = 0
                self.y += self.enemy_sprites.img_size/4
                self.direction = 1
            if self.y + image_size >= HEIGHT:
                self.y = HEIGHT - image_size
            if self.y < 0:
                self.y = 0
        else:
            self.out_of_bounds_group_handler(enemies)

    def out_of_bounds_group_handler(self, enemies: list):
        if len(enemies) > 0:

            if enemies[-1].x + image_size > WIDTH:
                enemies[-1].x = WIDTH - image_size
                self.change_enemies_group_directions(enemies, -1)
            if enemies[0].x < 0:
                enemies[0].x = 0
                self.change_enemies_group_directions(enemies, 1)

    def change_enemies_group_directions(self, enemies: list, new_direction):
        for enemy in enemies:
            enemy.y += enemy.enemy_sprites.img_size/4
            enemy.direction = new_direction
            # if enemy.y >= HEIGHT - image_size:
            #     enemies.remove(enemy)

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + 50) and (self.y - 50 <= bullet.y <= self.y + 50):
                self.hit_sfx.play()
                bullet.hit = True
                self.was_hit = True
                self.helth -= bullet.dmg_give
                # print("bullet dmg = ", bullet.dmg_give)
                self.hit_by_player_num = bullet.owner.player_num
                if self.current_hit_sfx < len(enemy_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
                # print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def show(self, window: Window):
        for bullet in self.en_bullets:
            bullet.collision_handler()
            bullet.show(window, self.bullet_speed, False)

            # print(bullet.y >= HEIGHT)
            if bullet.y >= HEIGHT-100 or bullet.hit:
                self.en_bullets.remove(bullet)

        self.enemy_animation.animate(window, self.x, self.y)
        # window.screen.blit(self.enemy_sprites.frames[0], (self.x, self.y))


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""" BOSS """


class Boss(Enemy):
    def __init__(self, boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown=40.0, worth=15, dmg_give=1, max_helth=50):
        super(Boss, self).__init__(boom, boss_sprites, x, y, bullet_sprites, shoot_cooldown, worth, dmg_give, max_helth)
        self.defeated = False
        self.fighting = False
        self.boss_bar = boss_bar
        self.step = self.helth // (len(self.boss_bar.frames) - 1)
        self.max_helth = self.helth

    def update(self, bullet_list):
        pass

    def get_health_percent(self):
        return (self.helth * 100) / self.max_helth

    def show(self, window: Window):
        for bullet in self.en_bullets:
            bullet.collision_handler()
            bullet.show(window, self.bullet_speed, False)

            # print(bullet.y >= HEIGHT)
            if bullet.y >= HEIGHT-100 or bullet.hit:
                self.en_bullets.remove(bullet)

        # everything after that loop depends on the boss


class FirstBoss(Boss):  # ANGRY ALIEN BOSS
    def __init__(self, boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown=40.0, worth=1000, dmg_give=1, max_helth=50):
        super(FirstBoss, self).__init__(boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown, worth, dmg_give, max_helth)
        self.helth = 50
        self.max_helth = 50
        self.step = self.max_helth // len(boss_bar.frames)
        self.boss_bar_frame = 0
        self.defeated = False

    def boss_bar_handler(self):
        if self.get_health_percent() == 100:
            self.boss_bar_frame = 0
        elif 70 < self.get_health_percent() <= 80:
            self.boss_bar_frame = 1
        elif 60 < self.get_health_percent() <= 70:
            self.boss_bar_frame = 2
        elif 30 < self.get_health_percent() <= 50:
            self.boss_bar_frame = 3
        elif self.get_health_percent() <= 30:
            self.boss_bar_frame = 4

    def update(self, bullet_list):
        current_time = pygame.time.get_ticks()
        if self.y + boss_image_size < HEIGHT:
            if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
                self.timer += 1
                self.last_update = current_time
                if self.timer >= self.shoot_cooldown:
                    # play shoot sfx
                    self.sfx.play()
                    # shoot
                    self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y, self.dmg_give))
                    self.timer = 0

        self.x += (self.move_speed * self.direction)

        self.boss_bar_handler()
        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler()

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + boss_image_size-50) and (self.y - 50 <= bullet.y <= self.y + boss_image_size/2):
                self.hit_sfx.play()
                bullet.hit = True
                self.was_hit = True
                self.helth -= bullet.dmg_give
                self.hit_by_player_num = bullet.owner.player_num
                if self.current_hit_sfx < len(enemy_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
                # print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def out_of_bounds_handler(self):
        if self.x + boss_image_size > WIDTH:
            self.x = WIDTH - boss_image_size
            self.direction = -1
        if self.x < 0:
            self.x = 0
            self.direction = 1
        if self.y + boss_image_size >= HEIGHT:
            self.y = HEIGHT - boss_image_size
        if self.y < 0:
            self.y = 0

    def show(self, window: Window):
        super(FirstBoss, self).show(window)

        window.screen.blit(self.enemy_sprites.frames[0], (self.x, self.y))
        window.screen.blit(self.boss_bar.frames[self.boss_bar_frame], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))


class SecondBoss(Boss):  # OCTOPUS BOSS
    def __init__(self, boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown=40.0, worth=1000, dmg_give=2, max_helth=100):
        super(SecondBoss, self).__init__(boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown, worth, dmg_give, max_helth)
        self.helth = 100
        self.animation = Animation(boss_sprites, 300)
        self.max_helth = 100
        self.step = self.max_helth // len(boss_bar.frames)
        self.boss_bar_frame = 0

        """
            kombinacije:
            x | 0  0  1 -1
            --+-----------
            y | 1 -1  0  0
        """
        self.direction_x = 1  # 0, 1, -1
        self.direction_y = 0  # 0, 1, -1
        self.directions = [1, 0]  # x, y
        self.defeated = False

    def boss_bar_handler(self):
        if self.get_health_percent() == 100:
            self.boss_bar_frame = 0
        elif 70 < self.get_health_percent() <= 80:
            self.boss_bar_frame = 1
        elif 60 < self.get_health_percent() <= 70:
            self.boss_bar_frame = 2
        elif 30 < self.get_health_percent() <= 50:
            self.boss_bar_frame = 3
        elif self.get_health_percent() <= 30:
            self.boss_bar_frame = 4

    def update(self, bullet_list):
        current_time = pygame.time.get_ticks()
        if self.y + boss_image_size < HEIGHT:
            if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
                self.timer += 1
                self.last_update = current_time
                if self.timer >= self.shoot_cooldown:
                    # play shoot sfx
                    self.sfx.play()
                    # shoot
                    self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y, self.dmg_give))
                    self.timer = 0

        self.x += (self.move_speed * self.directions[0])
        self.y += (self.move_speed * self.directions[1])

        self.boss_bar_handler()
        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler()

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + boss_image_size-50) and (self.y - 50 <= bullet.y <= self.y + boss_image_size/2):
                self.hit_sfx.play()
                bullet.hit = True
                self.was_hit = True
                self.helth -= bullet.dmg_give
                self.hit_by_player_num = bullet.owner.player_num
                if self.current_hit_sfx < len(enemy_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
                # print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def out_of_bounds_handler(self):
        if self.x + boss_image_size > WIDTH:
            self.x = WIDTH - boss_image_size
            self.directions[0] = -1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.x < 0:
            self.x = 0
            self.directions[0] = 1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.y + boss_image_size >= HEIGHT:
            self.y = HEIGHT - boss_image_size
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = -1
        if self.y < 0:
            self.y = 0
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = 1

    def show(self, window: Window):
        super(SecondBoss, self).show(window)

        self.animation.animate(window, self.x, self.y)
        window.screen.blit(self.boss_bar.frames[self.boss_bar_frame], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))
        # window.screen.blit(self.enemy_sprites.frames[0], (self.x, self.y))


class ThirdBoss(Boss):  # ROBOT BOSS
    def __init__(self, boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown=40.0, worth=1000, dmg_give=3, max_helth=150):
        super(ThirdBoss, self).__init__(boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown, worth, dmg_give, max_helth)
        self.helth = 150
        # self.animation = Animation(boss_sprites, 300)
        self.max_helth = 150
        self.step = self.max_helth // len(boss_bar.frames)
        self.boss_bar_frame = 0

        self.direction_x = 1  # 0, 1, -1
        self.direction_y = 0  # 0, 1, -1
        self.directions = [1, 0]  # x, y
        self.break_step = self.helth // 3

        self.current_frame = 0
        self.defeated = False

    def boss_bar_handler(self):
        if self.get_health_percent() == 100:
            self.boss_bar_frame = 0
        elif 70 < self.get_health_percent() <= 80:
            self.boss_bar_frame = 1
        elif 60 < self.get_health_percent() <= 70:
            self.boss_bar_frame = 2
        elif 30 < self.get_health_percent() <= 50:
            self.boss_bar_frame = 3
        elif self.get_health_percent() <= 30:
            self.boss_bar_frame = 4

    def update(self, bullet_list):
        current_time = pygame.time.get_ticks()
        if self.y + boss_image_size < HEIGHT:
            if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
                self.timer += 1
                self.last_update = current_time
                if self.timer >= self.shoot_cooldown:
                    # play shoot sfx
                    self.sfx.play()
                    # shoot
                    self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y, self.dmg_give))
                    self.timer = 0

        self.x += (self.move_speed * self.directions[0])
        self.y += (self.move_speed * self.directions[1])

        for i in range(0, 3):
            if i * self.break_step <= self.max_helth < (i + 1) * self.break_step:
                if i == 1:
                    self.current_frame = random.randint(1, 2)
                elif i == 2:
                    self.current_frame = 3
                else:
                    self.current_frame = i

        self.boss_bar_handler()
        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler()

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + boss_image_size-50) and (self.y - 50 <= bullet.y <= self.y + boss_image_size/2):
                self.hit_sfx.play()
                bullet.hit = True
                self.was_hit = True
                self.helth -= bullet.dmg_give
                self.hit_by_player_num = bullet.owner.player_num
                if self.current_hit_sfx < len(enemy_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
                # print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def out_of_bounds_handler(self):
        if self.x + boss_image_size > WIDTH:
            self.x = WIDTH - boss_image_size
            self.directions[0] = -1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.x < 0:
            self.x = 0
            self.directions[0] = 1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.y + boss_image_size >= HEIGHT:
            self.y = HEIGHT - boss_image_size
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = -1
        if self.y < 0:
            self.y = 0
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = 1

    def show(self, window: Window):
        super(ThirdBoss, self).show(window)

        # self.animation.animate(window, self.x, self.y)
        window.screen.blit(self.enemy_sprites.frames[self.current_frame], (self.x, self.y))
        window.screen.blit(self.boss_bar.frames[self.boss_bar_frame], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))


class FourthBoss(Boss):  # EYE BOSS
    def __init__(self, boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown=40.0, worth=1000, dmg_give=4, max_helth=200):
        super(FourthBoss, self).__init__(boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown, worth, dmg_give, max_helth)
        self.helth = 200
        # self.animation = Animation(boss_sprites, 300)
        self.max_helth = 200
        self.step = self.max_helth // len(boss_bar.frames)
        self.boss_bar_frame = 0

        self.direction_x = 1  # 0, 1, -1
        self.direction_y = 0  # 0, 1, -1
        self.directions = [1, 0]  # x, y
        self.full_helth = self.helth

        self.current_frame = 0
        self.dir_index = 0
        self.defeated = False

    def boss_bar_handler(self):
        if self.get_health_percent() == 100:
            self.boss_bar_frame = 0
        elif 70 < self.get_health_percent() <= 80:
            self.boss_bar_frame = 1
        elif 60 < self.get_health_percent() <= 70:
            self.boss_bar_frame = 2
        elif 30 < self.get_health_percent() <= 50:
            self.boss_bar_frame = 3
        elif self.get_health_percent() <= 30:
            self.boss_bar_frame = 4

    def update(self, bullet_list):
        current_time = pygame.time.get_ticks()
        if self.y + boss_image_size < HEIGHT:
            if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
                self.timer += 1
                self.last_update = current_time
                if self.timer >= self.shoot_cooldown:
                    # play shoot sfx
                    self.sfx.play()
                    # shoot
                    self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y, self.dmg_give))
                    self.timer = 0

        self.x += (self.move_speed * self.directions[0])
        self.y += (self.move_speed * self.directions[1])

        # calculate the current frame
        if self.directions[0] == -1:  # levo
            self.current_frame = 1
        elif self.directions[0] == 1:  # desno
            self.current_frame = 2

        if self.directions[1] == -1:  # gor
            self.current_frame = 4
        elif self.directions[1] == 1:  # dol
            self.current_frame = 3

        if self.directions[0] == 0 and self.directions[1] == 0:
            self.current_frame = 0

        self.boss_bar_handler()
        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler()

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + boss_image_size-50) and (self.y - 50 <= bullet.y <= self.y + boss_image_size/2):
                self.hit_sfx.play()
                bullet.hit = True
                self.was_hit = True
                self.helth -= bullet.dmg_give
                self.hit_by_player_num = bullet.owner.player_num
                if self.current_hit_sfx < len(enemy_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
                # print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def out_of_bounds_handler(self):
        if self.x + boss_image_size > WIDTH:
            self.x = WIDTH - boss_image_size
            self.directions[0] = -1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.x < 0:
            self.x = 0
            self.directions[0] = 1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.y + boss_image_size >= HEIGHT:
            self.y = HEIGHT - boss_image_size
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = -1
        if self.y < 0:
            self.y = 0
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = 1

    def show(self, window: Window):
        super(FourthBoss, self).show(window)

        window.screen.blit(self.enemy_sprites.frames[self.current_frame], (self.x, self.y))
        window.screen.blit(self.boss_bar.frames[self.boss_bar_frame], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))


class FinalBoss(Boss):  # SHIP BOSS
    def __init__(self, boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown=40.0, worth=5000, dmg_give=5, max_helth=250):
        super(FinalBoss, self).__init__(boom, boss_bar, boss_sprites, x, y, bullet_sprites, shoot_cooldown, worth, dmg_give, max_helth)
        self.helth = 250
        # self.animation = Animation(boss_sprites, 300)
        self.max_helth = 250
        self.step = self.max_helth // len(boss_bar.frames)
        self.boss_bar_frame = 0

        self.directions = [1, 0]  # x, y
        self.current_frame = 0
        self.move_speed = 4
        self.defeated = False

    def boss_bar_handler(self):
        if self.get_health_percent() == 100:
            self.boss_bar_frame = 0
        elif 70 < self.get_health_percent() <= 80:
            self.boss_bar_frame = 1
        elif 60 < self.get_health_percent() <= 70:
            self.boss_bar_frame = 2
        elif 30 < self.get_health_percent() <= 50:
            self.boss_bar_frame = 3
        elif self.get_health_percent() <= 30:
            self.boss_bar_frame = 4

    def update(self, bullet_list):
        current_time = pygame.time.get_ticks()
        if self.y + boss_image_size < HEIGHT:
            if current_time - self.last_update >= self.shoot_cooldown:  # if 500 ms have passed, move on to the next frame
                self.timer += 1
                self.last_update = current_time
                if self.timer >= self.shoot_cooldown:
                    # play shoot sfx
                    self.sfx.play()
                    # shoot
                    self.en_bullets.append(pc.Bullet(self.bullet_sprites, self, self.x, self.y, self.dmg_give))
                    self.timer = 0

        self.x += (self.move_speed * self.directions[0])
        self.y += (self.move_speed * self.directions[1])

        # calculate the current frame
        if self.directions[0] == -1:
            self.current_frame = 2
        elif self.directions[0] == 1:
            self.current_frame = 1
        elif self.directions[0] == 0:
            self.current_frame = 0

        self.boss_bar_handler()
        self.bullet_collision_handler(bullet_list)
        self.out_of_bounds_handler()

    def bullet_collision_handler(self, bullet_list):
        for bullet in bullet_list:
            if (self.x - 50 <= bullet.x <= self.x + boss_image_size-50) and (self.y - 50 <= bullet.y <= self.y + boss_image_size/2):
                self.hit_sfx.play()
                bullet.hit = True
                self.was_hit = True
                self.helth -= bullet.dmg_give
                self.hit_by_player_num = bullet.owner.player_num
                if self.current_hit_sfx < len(enemy_hit_sfxs) - 1:
                    self.current_hit_sfx += 1
                else:
                    self.current_hit_sfx = 0
                self.hit_sfx = pygame.mixer.Sound(enemy_hit_sfxs[self.current_hit_sfx])
                # print(self.helth)
            else:
                continue
                # bullet.hit = False
                # self.was_hit = False

    def out_of_bounds_handler(self):
        if self.x + boss_image_size > WIDTH:
            self.x = WIDTH - boss_image_size
            self.directions[0] = -1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.x < 0:
            self.x = 0
            self.directions[0] = 1
            self.directions[1] = random.randrange(-1, 2, 1)
        if self.y + boss_image_size >= HEIGHT:
            self.y = HEIGHT - boss_image_size
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = -1
        if self.y < 0:
            self.y = 0
            self.directions[0] = random.randrange(-1, 2, 1)
            self.directions[1] = 1

    def show(self, window: Window):
        super(FinalBoss, self).show(window)

        window.screen.blit(self.enemy_sprites.frames[self.current_frame], (self.x, self.y))
        window.screen.blit(self.boss_bar.frames[self.boss_bar_frame], (BOSS_IMAGE_SCALE + WIDTH / 2.25, BOSS_IMAGE_SCALE))


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Enemies:
    def __init__(self, enemies_2d_array):
        self.enemies_2d_array = enemies_2d_array
        # self.enemies = []

    def update(self, bullet_list):
        self.bullet_collision_handler(bullet_list)
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                enemy.update(bullet_list, True)
        self.out_of_bounds_handler()

    def out_of_bounds_handler(self):
        for enemies in self.enemies_2d_array:
            if len(enemies) > 0:
                if enemies[-1].x + image_size > WIDTH:
                    enemies[-1].x = WIDTH - image_size
                    self.change_all_directions(-1)
                if enemies[0].x < 0:
                    enemies[0].x = 0
                    self.change_all_directions(1)
                # if self.enemies_2d_array[-1][0].y + image_size >= HEIGHT:
                #     self.enemies_2d_array[-1][0].y = HEIGHT - image_size
                # if self.enemies_2d_array[0][0].y < 0:
                #     self.enemies_2d_array[0][0].y = 0

    def change_all_directions(self, new_direction):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                enemy.direction = new_direction

    def helth_check(self):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                # print(enemy.helth)
                if enemy.helth <= 0:
                    enemies.remove(enemy)

    def update_2d_array(self, new_2d):
        self.enemies_2d_array = new_2d

    def bullet_collision_handler(self, bullet_list):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                if len(enemies) > 0:
                    enemy.bullet_collision_handler(bullet_list)
                # for bullet in bullet_list:
                #     if (enemy.x - 50 <= bullet.x <= enemy.x + 50) and bullet.y <= enemy.y + 50:
                #         bullet.hit = True
                #         enemy.was_hit = True
                #         # self.helth -= 1
                #         print(enemy.helth)
                #     else:
                #         bullet.hit = False
                #         enemy.was_hit = False

    def show(self, window: Window):
        for enemies in self.enemies_2d_array:
            for enemy in enemies:
                enemy.show(window)

