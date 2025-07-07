import pygame

from .animations import idle, walk

class Character_state:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.frame_type = idle

    def character_movement(self, keys):
     if keys[pygame.K_d]:
            self.direction = 0
            self.frame_type = walk[self.direction]
            self.x = self.x + 1

     elif keys[pygame.K_a]:
            self.direction = 1
            self.frame_type = walk[self.direction]
            self.x = self.x - 1

     elif keys[pygame.K_s]:
            self.direction = 2
            self.frame_type = walk[self.direction]
            self.y = self.y + 1
    
     elif keys[pygame.K_w]:
            self.direction = 3
            self.frame_type = walk[self.direction]
            self.y = self.y - 1

     else:
            self.frame_type = idle[self.direction]