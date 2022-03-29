import pygame
import time

# init
pygame.init()

pygame.joystick.init()
joysticks = set()
player_num = 2

joysticks_list = []
while True:
    if len(joysticks) != player_num:
        for i in range(pygame.joystick.get_count()):
            print("here")
            joysticks_list.append((pygame.joystick.Joystick(i), pygame.joystick.Joystick(i).get_instance_id()))
            pygame.joystick.Joystick(i).init()

            time.sleep(1)
            print(set(joysticks_list))

    # joysticks_list = list(joysticks)
    # print(joysticks_list)

