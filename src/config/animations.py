import pygame
from .constants import GIRL_FRAME_HEIGHT, GIRL_FRAME_WIDTH
import os

def load_frames(sheet, frame_width, frame_height, num_frames):
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

LILY_IDLE_IMAGE = pygame.image.load(
    os.path.join('Assets','Girl','Idle.png')
)
LILY_WALK_RIGHT_IMAGE = pygame.image.load(
    os.path.join('Assets','Girl','Walk.png')
)

idle_frames = load_frames(LILY_IDLE_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,2)
walkr_frames = load_frames(LILY_WALK_RIGHT_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,6)