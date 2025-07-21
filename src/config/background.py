import pygame
import os
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_HEIGHT, TILE_WIDTH

LEVEL1_BG_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join('Assets','Background','level1-bg.png')), (SCREEN_WIDTH, SCREEN_HEIGHT))

# temple_tile = pygame.image.load(os.path.join('Assets','Level_2','Temple_Tile.png')).convert()