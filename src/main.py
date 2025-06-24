import pygame
import os

import config.color         #import colors from color.py
import config.constants     #import constants from constants.py
from config.animations import idle_frames, walkr_frames

frame_timer = 0
frame_index = 0

pygame.init()

#1. Game Window
SCREEN = pygame.display.set_mode((config.constants.SCREEN_WIDTH, config.constants.SCREEN_HEIGHT))
pygame.display.set_caption("Lily's Adventure")


def draw_window():
    global frame_timer
    global frame_index
    frame_timer = (frame_timer + 1) 
    if frame_timer==10:
        frame_index = (frame_index + 1) % 6
        frame_timer = 0
    print(frame_timer)
    SCREEN.fill(config.color.BLACK)
    SCREEN.blit(walkr_frames[frame_index],(600,350))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

#2. Game Loop
    run = True
    while run:
        clock.tick(config.constants.FPS)                 #LIMIT FPS
#3. Game Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            
        draw_window()
            
    pygame.quit()

if __name__ == '__main__':
    main()
