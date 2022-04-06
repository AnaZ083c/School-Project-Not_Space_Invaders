import constants_and_globals as cag
import pygame


class Window:
    running = True

    def __init__(self):
        # self.init_consts()

        self.width = cag.WIDTH
        self.height = cag.HEIGHT
        self.bg_color = cag.BLACK
        self.screen = None
        self.clock = None

    def init_consts(self):
        info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()
        cag.WIDTH = info.current_w
        cag.HEIGHT = info.current_h
        cag.scale_x: float = cag.WIDTH / cag.WIDTH_FIXED
        cag.scale_y: float = cag.HEIGHT / cag.HEIGHT_FIXED
        cag.scale: float = max(cag.scale_x, cag.scale_y)
        cag.IMAGE_SCALE: float = cag.scale / 2  # 0.5
        cag.BOSS_IMAGE_SCALE: float = cag.scale * 1.0
        cag.FONT_SCALE = cag.scale * 1.0
        cag.FRAME_OFFSET: int = 256

        cag.image_size = (cag.FRAME_OFFSET * cag.IMAGE_SCALE)
        cag.boss_image_size = (cag.FRAME_OFFSET * cag.BOSS_IMAGE_SCALE)

    def init_window(self):
        print(f"{cag.WIDTH} x {cag.HEIGHT}")

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        # self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Definitely Not Space Invaders')
        self.clock = pygame.time.Clock()

        # window.fill(self.bg_color)
        # pygame.display.flip()

