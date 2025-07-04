import pygame
import os
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT

LEVEL1_BG= pygame.image.load(os.path.join('Assets','level1-bg.png'))
LEVEL1_BG_IMAGE= pygame.transform.scale(LEVEL1_BG, (SCREEN_WIDTH, SCREEN_HEIGHT))