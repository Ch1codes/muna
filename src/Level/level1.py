import pygame
import os
import random
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT

SKELETONS= []
SKELETONS_X= []
SKELETONS_Y= []
NO_of_SKELETONS= 6

    

def preload():
    global LEVEL1_BG_IMAGE, BUFFER
    
    LEVEL1_BG= pygame.image.load(os.path.join('Assets','level1-bg.png')).convert()
    LEVEL1_BG_IMAGE= pygame.transform.scale(LEVEL1_BG, (1400, 900))

    # SKELETONS= pygame.image.load(os.path.join('Assets','skeletons.png')).convert_alpha()
    # SKELETONS_IMG= pygame.transform.scale(SKELETONS, (50,50))

    # SKELETONS_X= random.randint(400,1350)
    # SKELETONS_Y= random.randint(50,850)
    
    for skeletons in range(NO_of_SKELETONS):
        SKELETONS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets','skeletons.png')).convert_alpha(), (50,50)))
        SKELETONS_X.append(random.randint(400,1350))
        SKELETONS_Y.append(random.randint(50,850))

    BUFFER = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    BUFFER.blit(LEVEL1_BG_IMAGE, (0, 0))


def draw(SCREEN, chara_frame,pos, frame_timer):
    SCREEN.blit(BUFFER, (0,0))
    for i in range(NO_of_SKELETONS):
        SCREEN.blit(SKELETONS[i], (SKELETONS_X[i], SKELETONS_Y[i]))
    
    SCREEN.blit(chara_frame.animate(frame_timer),(pos.x,pos.y))
    
    pygame.display.update()


    