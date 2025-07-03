import pygame
import os
# from ..config.constants import SCREEN_WIDTH, SCREEN_HEIGHT

LEVEL1_BG= pygame.image.load(os.path.join('Assets','level1-bg.png'))
LEVEL1_BG_IMAGE= pygame.transform.scale(LEVEL1_BG, (1400, 900))

def draw(SCREEN):
    SCREEN.blit(LEVEL1_BG_IMAGE, (0,0))
    
    # pygame.display.update()
