import pygame
from .constants import GIRL_FRAME_HEIGHT, GIRL_FRAME_WIDTH, FPS
import os

class Animation:
    def __init__(self,name,n):
        self.frame_name = name
        self.no_of_frames = n
        self.frame_index = 0

    def animate(self,timer):
        if(timer%(FPS/self.no_of_frames)==0):
            self.frame_index = (self.frame_index+1)%self.no_of_frames
        return self.frame_name[self.frame_index]

def load_frames(sheet, frame_width, frame_height, num_frames):
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
        frames.append(frame)
    return frames

IDLE_FRAMES_N = 2
WALKLR_FRAMES_N = 6

LILY_IDLE_IMAGE = pygame.image.load(
    os.path.join('Assets','Girl','Idle.png')
)

LILY_WALK_RIGHT_IMAGE = pygame.image.load(
    os.path.join('Assets','Girl','Walk.png')
)

idle_frames = load_frames(LILY_IDLE_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,IDLE_FRAMES_N)
walkr_frames = load_frames(LILY_WALK_RIGHT_IMAGE, GIRL_FRAME_WIDTH, GIRL_FRAME_HEIGHT,WALKLR_FRAMES_N)
walkl_frames = [1,2,3,4,5,6]

for i in range(len(walkr_frames)):
    walkl_frames[i] = pygame.transform.flip(walkr_frames[i], True, False) 

idle = Animation(idle_frames,IDLE_FRAMES_N)
walkr = Animation(walkr_frames,WALKLR_FRAMES_N)
walkl = Animation(walkl_frames,WALKLR_FRAMES_N)
