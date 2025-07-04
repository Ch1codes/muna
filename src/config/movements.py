import pygame

from .animations import idle, walk

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def character_movement(keys, direction, pos):
    if keys[pygame.K_d]:
            direction[0] = 0
            frame_type = walk[direction[0]]
            pos.x = pos.x + 1

    elif keys[pygame.K_a]:
            direction[0] = 1
            frame_type = walk[direction[0]]
            pos.x = pos.x - 1

    elif keys[pygame.K_s]:
            direction[0] = 2
            frame_type = walk[direction[0]]
            pos.y = pos.y + 1
    
    elif keys[pygame.K_w]:
            direction[0] = 3
            frame_type = walk[direction[0]]
            pos.y = pos.y - 1

    else:
            frame_type = idle[direction[0]]
    
    return frame_type