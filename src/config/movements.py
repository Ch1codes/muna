import pygame

from .animations import idle, walk, shoot
from .constants import WALK_SPEED, GIRL_FRAME_HEIGHT, GIRL_FRAME_WIDTH, HITBOX_WIDTH, HITBOX_HEIGHT

class Character_state:
       def __init__(self, x, y, bound):
              self.x = x
              self.y = y
              self.direction = 0
              self.frame_type = idle[self.direction]
              self.hitbox = pygame.Rect(self.x, self.y, HITBOX_WIDTH, HITBOX_HEIGHT)
              self.bound = bound
              self.timer = 0

       def character_movement(self, keys):
              if not self.hitbox.collidelistall(self.bound):

                     if self.frame_type != shoot:
                            if keys[pygame.K_SPACE]:
                                   self.direction = 0
                                   self.frame_type = shoot

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

                            elif keys[pygame.K_RIGHT]:
                                   self.direction = 0
                                   self.frame_type = walk[self.direction]
                                   self.x = self.x + WALK_SPEED

                            else:
                                   self.frame_type = idle[self.direction]
                                   for walkd in walk:
                                          walkd.timer = 0
                     else:  
                            if shoot.timer == 59:
                                   shoot.timer = 0
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
              self.hitbox.update(self.x + (GIRL_FRAME_WIDTH - HITBOX_WIDTH)/2 , self.y + (GIRL_FRAME_HEIGHT - HITBOX_HEIGHT)-20, HITBOX_WIDTH, HITBOX_HEIGHT)

