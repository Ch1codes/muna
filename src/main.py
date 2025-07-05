import pygame
import os

import config.color         #import colors from color.py
from config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, GIRL_FRAME_HEIGHT, GIRL_FRAME_WIDTH    #import constants from constants.py
from config.animations import idle, walkr, walkl
from config.movement import movement, Position
import Level.level1
pygame.init()

#1. Game Window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lily's Adventure")


# def draw_window(chara_frame,pos, frame_timer):

#     SCREEN.blit(chara_frame.animate(frame_timer),(pos.x,pos.y))
#     pygame.display.update()

def load_assets():
    Level.level1.preload()

def main():
    clock = pygame.time.Clock()
    
    load_assets()
    
    #player_pos not needed, should be defined in each levels
    player_pos = Position(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    frame_timer = 0

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

        frame_type, player_pos = movement(player_pos)
        
        Level.level1.draw(SCREEN, frame_type, player_pos, frame_timer)
        
        #draw_window(frame_type, player_pos, frame_timer)
        frame_timer = (frame_timer + 1) % FPS
        
            
    pygame.quit()

if __name__ == '__main__':
    main()
