import pygame
import os

import config.color         #import colors from color.py
from config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH    #import constants from constants.py
from config.animations import idle, walkr, walkl

frame_timer = 0
frame_index = 0

pygame.init()

#1. Game Window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lily's Adventure")


def draw_window(chara_frame):
    global frame_timer
    global frame_index
    frame_timer = (frame_timer + 1) % FPS
    print(frame_timer)
    SCREEN.fill(config.color.BLACK)

    SCREEN.blit(chara_frame.animate(frame_timer),(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

#2. Game Loop
    run = True
    while run:
        clock.tick(FPS)                 #LIMIT FPS
#3. Game Event Handler


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        frame_type = idle

        if keys[pygame.K_d]:
            print("d key is being pressed!")
            frame_type = walkr

        if keys[pygame.K_a]:
            print("a key is being pressed!")
            frame_type = walkl
            
        draw_window(frame_type)
            
    pygame.quit()

if __name__ == '__main__':
    main()
