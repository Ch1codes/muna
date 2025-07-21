import pygame

from src.config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH  #import constants from constants.py
from src.Level import level1
from src.Level import level2

pygame.init()



#1. Game Window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
print("screen blited")
pygame.display.set_caption("Lily's Adventure")

def load_assets():
    level1.preload()

def main():
    clock = pygame.time.Clock()
    
            
    level = 1
    load_assets()

#2. Game Loop
    run = True
    while run:
        clock.tick(FPS)                 #LIMIT FPS
#3. Game Event Handler

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()               

        match level:
            case 1:
                L1=level1.draw(SCREEN, keys)
                if L1:
                    level = 2
                    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT))
            case 2:
                L2=level2.draw(SCREEN)
                if L2:
                    level = 3
            case 3:
                x = input("")
                run = False
                pass

    pygame.quit()

if __name__ == '__main__':
    main()
