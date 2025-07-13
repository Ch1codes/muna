import pygame
import os
import random
from ..config.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from ..config.movements import Character_state
from ..config.map import load_map
from ..config import map_sketch

SKELETONS= []
SKELETONS_X= []
SKELETONS_Y= []
SKELETONSX_CHANGE= []
SKELETONSY_CHANGE= []
NO_of_SKELETONS= 6
BORDER_POS = 350

BORDER= pygame.Rect(BORDER_POS, 0, 5, SCREEN_HEIGHT)
BLACK= (0,0,0)

BOUND = load_map(map_sketch.map_level1)

character_state=Character_state(BORDER_POS-50, SCREEN_HEIGHT/2, BOUND)
     

def preload():
    global LEVEL1_BG_IMAGE, BUFFER
    
    LEVEL1_BG= pygame.image.load(os.path.join('Assets','Background','level1-bg.png')).convert()
    LEVEL1_BG_IMAGE= pygame.transform.scale(LEVEL1_BG, (1400, 900))
    
    
    
    for skeletons in range(NO_of_SKELETONS):
        SKELETONS.append(pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'Background' ,'skeletons.png')).convert_alpha(), (50,50)))
        SKELETONS_X.append(random.randint(400,1350))
        SKELETONS_Y.append(random.randint(50,850))
        SKELETONSX_CHANGE.append(40)
        SKELETONSY_CHANGE.append(1)

    BUFFER = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    BUFFER.blit(LEVEL1_BG_IMAGE, (0, 0))

def draw(SCREEN, frame_timer, keys):
    
    # if character_state.x>0 and character_state.x<1350:
    character_state.character_movement(keys)
    
    SCREEN.blit(BUFFER, (0,0))
    for i in range(NO_of_SKELETONS):
        SCREEN.blit(SKELETONS[i], (SKELETONS_X[i], SKELETONS_Y[i]))
        
        SKELETONS_Y[i] += SKELETONSY_CHANGE[i]
        
        if SKELETONS_Y[i] > 850:
            SKELETONSY_CHANGE[i]= -1
            SKELETONS_X[i] -= SKELETONSX_CHANGE[i]
            
        elif SKELETONS_Y[i] < 0:
            SKELETONSY_CHANGE[i]= 1
            SKELETONS_X[i] -= SKELETONSX_CHANGE[i]
            
    
    SCREEN.blit(character_state.frame_type.animate(frame_timer),(character_state.x,character_state.y))
    # pygame.draw.rect(SCREEN, BLACK, character_state.hitbox)
    # pygame.draw.rect(SCREEN, BLACK, BORDER)
    
    pygame.display.update()