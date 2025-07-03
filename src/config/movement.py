import pygame

from config.constants import SCREEN_HEIGHT, SCREEN_WIDTH, GIRL_FRAME_HEIGHT, GIRL_FRAME_WIDTH    #import constants from constants.py
from config.animations import idle, walkr, walkl

class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def movement(Pos):
    player_pos = Position(Pos.x,Pos.y)

    keys = pygame.key.get_pressed()
    frame_type = idle
    if keys[pygame.K_d]:
            
            frame_type = walkr
            
            if player_pos.x < SCREEN_WIDTH- GIRL_FRAME_WIDTH:
                player_pos.x = player_pos.x + 2

    if keys[pygame.K_a]:
            
            frame_type = walkl
            if player_pos.x > 0:
                player_pos.x = player_pos.x - 2
                
    return frame_type, player_pos