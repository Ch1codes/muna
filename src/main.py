import pygame

import config.color         #import colors from color.py
from config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH    #import constants from constants.py
from config.movements import Character_state

pygame.init()

#1. Game Window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lily's Adventure")

def draw_window(character_state, frame_timer):
    SCREEN.fill(config.color.BLACK)
    SCREEN.blit(character_state.frame_type.animate(frame_timer),(character_state.x,character_state.y))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    frame_timer = 0
    character_state = Character_state(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0)      # original character position and direction ..... look at line 35
#2. Game Loop
    run = True
    while run:
        clock.tick(FPS)                 #LIMIT FPS
#3. Game Event Handler

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        character_state.character_movement(keys)                    # function is in movement.py..... line 22 required for this

        frame_timer = (frame_timer + 1) % FPS                      # frame counter ; may need to create a better way

        draw_window(
            character_state,
            frame_timer
            )                                                     # parameters (character movement update, fps counter)
            
    pygame.quit()

if __name__ == '__main__':
    main()
