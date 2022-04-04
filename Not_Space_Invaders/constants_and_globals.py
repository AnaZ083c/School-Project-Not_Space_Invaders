import pygame
# constants
pygame.init()
info = pygame.display.Info()  # You have to call this before pygame.display.set_mode()

FPS = 60
TITANIUM_HWHITE = (255, 255, 255)  # titanium Hwhite :P
NOT_CHOSEN = (130, 130, 130)
BLACK = (0, 0, 0)
BLACK_RED = (115, 100, 100)
BLACKER_RED = (78, 12, 12)

WIDTH_FIXED = 1920
HEIGHT_FIXED = 1080  # (1280, 1000)  # 1000, 900
WIDTH = info.current_w # WIDTH = 1600
HEIGHT = info.current_h # HEIGHT = 900

SPRITE_SHEET = 'assets/sprite-sheet08-transparent.png'
PLANETS_SPRITE_SHEET = 'assets/planets-sprite-sheet-2.png'
PLANET = 'assets/end.png'

PLAYER_RED_BULLET_SFX = 'assets/player_redBullet_shoot.mp3'
GENERIC_ENEMY_BULLET_SFX = 'assets/generic_enemy_shoot.mp3'
ENEMY_HIT_1 = 'assets/sfx/enemy-hit-1.wav'
ENEMY_HIT_2 = 'assets/sfx/enemy-hit-2.wav'
ENEMY_HIT_3 = 'assets/sfx/enemy-hit-3.wav'
ENEMY_EXPLODE = 'assets/sfx/enemy-explode-1.wav'
ICON = 'assets/not_space_invaders_icon.ico'

PLAYER_HIT_1 = 'assets/sfx/player-hit-1.wav'
PLAYER_HIT_2 = 'assets/sfx/player-hit-2.wav'
PLAYER_HIT_3 = 'assets/sfx/player-hit-3.wav'
PICKUP_1 = 'assets/sfx/pickup-1.wav'
PICKUP_2 = 'assets/sfx/pickup-2.wav'
PICKUP_3 = 'assets/sfx/pickup-3.wav'
PICKUP_4 = 'assets/sfx/pickup-4.wav'


THEME = 'assets/not_theme.mp3'
FONT = 'assets/fonts/Not_space_invaders_font-Regular.otf'

LEVELS = 'assets/levels/'
POINTS = 'assets/points/points.pts'

PLAYER1_COLOR = (17, 255, 0)
PLAYER2_COLOR = (0, 200, 255)

scale_x: float = WIDTH / WIDTH_FIXED
scale_y: float = HEIGHT / HEIGHT_FIXED
scale: float = max(scale_x, scale_y)
IMAGE_SCALE: float = scale / 2 # 0.5
BOSS_IMAGE_SCALE: float = scale * 1.0
PLANET_SCALE: float = scale * 1.0
FONT_SCALE = scale * 1.0
FRAME_OFFSET: int = 256

BULLET_W = 50
BULLET_H = 100

GREEN_B = 15
PURPLE_B = 10
BLUE_B = 10
YELLOW_B = 8
RED_B = 20

GENERIC_ENEMY_HP = 4
OCTOPUS_ENEMY_HP = 9
ROBOT_ENEMY_HP = 14

BOSS_1_HP = 100
BOSS_1_DMG = 2

BOSS_2_HP = 200
BOSS_2_DMG = 3

BOSS_3_HP = 300
BOSS_3_DMG = 4

BOSS_4_HP = 400
BOSS_4_DMG = 5

BOSS_5_HP = 500
BOSS_5_DMG = 6

SETTINGS = 'assets/settings/settings.txt'

# globals
planet_image_size = (FRAME_OFFSET * PLANET_SCALE)
image_size = (FRAME_OFFSET * IMAGE_SCALE)
boss_image_size = (FRAME_OFFSET * BOSS_IMAGE_SCALE)

star_colors = [
    (0, 113, 193),
    (153, 205, 255),
    (255, 255, 255),
    (254, 255, 153),
    (255, 255, 0),
    (255, 102, 0),
    (254, 0, 0)
]

star_sizes = [
    4,
    3,
    2,
    1,
    1,
    1,
    1
]

sound_state = 1
enemy_hit_sfxs = [ENEMY_HIT_1, ENEMY_HIT_2, ENEMY_HIT_3]
player_hit_sfxs = [PLAYER_HIT_1, PLAYER_HIT_2, PLAYER_HIT_3]
pickup_sfxs = [PICKUP_1, PICKUP_2, PICKUP_3, PICKUP_4]


