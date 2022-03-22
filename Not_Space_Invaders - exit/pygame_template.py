from Window import Window
import pygame

# constants and other vars
FPS = 60
WHITE = (255,255,255) # titanium white :P
(WIDTH, HEIGHT) = (800, 600)

# init
pygame.init()
pygame.mixer.init()

# window
window = Window()
window.init_window()

all_sprites = pygame.sprite.Group()
# game loop
while window.running:
    # keep loop running at FPS
    window.clock.tick(FPS)

    # process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # if X was clicked
            window.running = False

    # update
    all_sprites.update()

    # draw/render
    window.screen.fill(WHITE)
    all_sprites.draw(window.screen)
    pygame.display.flip() # always after drawing everything!!

pygame.quit() # close pygame