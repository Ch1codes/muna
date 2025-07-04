import pygame

import config.color         #import colors from color.py
from config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH    #import constants from constants.py
from config.movements import Position, character_movement

pygame.init()

#1. Game Window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lily's Adventure")

def draw_window(chara_frame, frame_timer, character_position):
    SCREEN.fill(config.color.BLACK)
    SCREEN.blit(chara_frame.animate(frame_timer),(character_position.x,character_position.y))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    frame_timer = 0
    direction = [0]
    character_position = Position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)      # original character position
#2. Game Loop
    run = True
    while run:
        clock.tick(FPS)                 #LIMIT FPS
#3. Game Event Handler

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        frame_type = character_movement(keys, direction, character_position)        # function is in movement.py 

        frame_timer = (frame_timer + 1) % FPS                                       # frame counter ; may need to create a better way

        draw_window(frame_type, frame_timer, character_position)                    # parameters (what frame to animate, fps counter, position of character)
            
    pygame.quit()

if __name__ == '__main__':
    main()
