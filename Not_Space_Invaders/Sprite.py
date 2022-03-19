from Window import Window
from constants_and_globals import *
import pygame

""" 
    Class for handling sprite sheets 
"""


class SpriteSheet:
    def __init__(self, filename):
        self.image = pygame.image.load(filename).convert_alpha()

    def get_image(self, frame, width, height, scale=1.0, xy_start=(0, 0)):
        (x_start, y_start) = xy_start
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        # image.blit(self.image, (0, 0), ((frame * width), y_start, width, height))
        image.blit(self.image, (0, 0), ((frame * width), y_start, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image


""" 
    Class for handling and initializing list of sprite objects;
    each game object has its own list of sprites 
"""
# each player has 3 frames


class Sprite:
    def __init__(self, sprite_sheet: SpriteSheet, num_of_frames: int = 3, xy_start=(0, 0), horizontal: bool = True,
                 scale: float = 0.5):
        self.sprite_sheet = sprite_sheet
        self.frames = []
        self.scale = scale  # IMAGE_SCALE
        self.img_size = FRAME_OFFSET * self.scale

        self.init_frames(horizontal, xy_start, num_of_frames)

    def init_frames(self, horizontal, xy_start=(0, 0), num_of_frames: int = 3):
        (x_start, y_start) = xy_start
        end_range = x_start + num_of_frames
        # a generic enemy only has one frame!
        if not horizontal:
            for i, j in zip(range(x_start, end_range), range(0, num_of_frames)):
                self.frames.append(
                    self.sprite_sheet.get_image(x_start, 256, 256, self.scale, (x_start, y_start + j * FRAME_OFFSET)))
        else:
            for i in range(x_start, end_range):
                self.frames.append(self.sprite_sheet.get_image(i, 256, 256, self.scale, (x_start, y_start)))

    def show_frames(self, window: Window, xy_tup=(0, 0)):
        (x, y) = xy_tup
        # print(len(self.frames))
        for i in range(0, len(self.frames)):
            window.screen.blit(self.frames[i], (x + ((FRAME_OFFSET * i) * self.scale), y))

    def set_scale(self, new_scale):
        self.scale = new_scale

    def rotate(self, angle: float):
        rotated_sprite_sheet = pygame.transform.rotate(self.sprite_sheet, angle)




"""
    Class for handling and generation animations
"""


class Animation:
    def __init__(self, sprite: Sprite, animation_cooldown: int = 500):
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = animation_cooldown
        self.sprite = sprite
        self.start_frame = 0
        self.end_frame = len(sprite.frames)
        self.stopped = False

    def animate(self, window: Window, x, y, loop: bool = True, keep_on_after_animation: bool = True):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:  # if 500 ms have passed, move on to the next frame
            self.start_frame += 1
            self.last_update = current_time
            if loop and (self.start_frame >= self.end_frame or self.start_frame >= len(self.sprite.frames)):
                self.start_frame = 0
            elif not loop and self.start_frame >= len(self.sprite.frames):
                self.start_frame = len(self.sprite.frames) - 1
                self.stopped = True

        # show frame image
        if not self.stopped:
            window.screen.blit(self.sprite.frames[self.start_frame], (x, y))

    def set_start_end_frame(self, new_start, new_end):
        self.start_frame = new_start
        self.end_frame = new_end
