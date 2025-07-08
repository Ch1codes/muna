import pygame

from .animations import idle, walk
from .constants import WALK_SPEED, GIRL_FRAME_HEIGHT, GIRL_FRAME_WIDTH

class Character_state:
       def __init__(self, x, y, bound):
              self.x = x
              self.y = y
              self.direction = 0
              self.frame_type = idle[self.direction]
              self.hitbox = pygame.Rect(self.x - 10, self.y - 10, GIRL_FRAME_WIDTH - 10, GIRL_FRAME_HEIGHT - 40)
              self.bound = bound

       def character_movement(self, keys):
              if not self.hitbox.collidelistall(self.bound):

                     if keys[pygame.K_RIGHT]:
                            self.direction = 0
                            self.frame_type = walk[self.direction]
                            self.x = self.x + WALK_SPEED

                     elif keys[pygame.K_LEFT]:
                            self.direction = 1
                            self.frame_type = walk[self.direction]
                            self.x = self.x - WALK_SPEED

                     elif keys[pygame.K_DOWN]:
                            self.direction = 2
                            self.frame_type = walk[self.direction]
                            self.y = self.y + WALK_SPEED
                     
                     elif keys[pygame.K_UP]:
                            self.direction = 3
                            self.frame_type = walk[self.direction]
                            self.y = self.y - WALK_SPEED

                     else:
                            self.frame_type = idle[self.direction] 
              else:
                     if self.direction == 0:
                            self.x = self.x - WALK_SPEED
                     elif self.direction == 1:
                            self.x = self.x + WALK_SPEED
                     elif self.direction == 2:
                            self.y = self.y - WALK_SPEED
                     else:
                            self.y = self.y + WALK_SPEED
              self.hitbox.update(self.x + 10, self.y + 80, GIRL_FRAME_WIDTH - 20, GIRL_FRAME_HEIGHT - 80)