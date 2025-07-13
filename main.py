import pygame

from src.config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH  #import constants from constants.py
from src.Level import level1

pygame.init()


#1. Game Window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
print("screen blited")
pygame.display.set_caption("Lily's Adventure")

def load_assets():
    level1.preload()

def main():
    clock = pygame.time.Clock()
    
    load_assets()

    frame_timer = 0
#2. Game Loop
    run = True
    while run:
        clock.tick(FPS)                 #LIMIT FPS
#3. Game Event Handler

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()               
        
        level1.draw(SCREEN, frame_timer, keys)

        frame_timer = (frame_timer + 1) % FPS                      # frame counter ; may need to create a better way

    pygame.quit()

if __name__ == '__main__':
    main()
