import pygame
import os

from src.config.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from src.Level import level1
from src.Level import level2
from src.Level import level3

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Muna's Adventure")

def draw_outlined_text(surface, text, font, pos, text_color, outline_color=(0, 0, 0)):
    x, y = pos
    for dx in [-2, -1, 0, 1, 2]:
        for dy in [-2, -1, 0, 1, 2]:
            if dx != 0 or dy != 0:
                outline = font.render(text, True, outline_color)
                outline_rect = outline.get_rect(center=(x + dx, y + dy))
                surface.blit(outline, outline_rect)
    rendered_text = font.render(text, True, text_color)
    text_rect = rendered_text.get_rect(center=pos)
    surface.blit(rendered_text, text_rect)

def main():
    clock = pygame.time.Clock()
    run = True
    state = 'start'

    # Load intro assets
    intro_bg1 = pygame.image.load('Assets/level1/level1intro.png').convert()
    intro_bg1 = pygame.transform.scale(intro_bg1, (SCREEN_WIDTH, SCREEN_HEIGHT))
    intro_bg2 = pygame.image.load('Assets/level1/level2intro.png').convert()
    intro_bg2 = pygame.transform.scale(intro_bg2, (SCREEN_WIDTH, SCREEN_HEIGHT))

    font_path = os.path.join('Assets', 'level3', 'font', 'Pixeltype.ttf')
    intro_font = pygame.font.Font(font_path, 54)
    large_font = pygame.font.Font(font_path, 108)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

   
        if state == 'start':
            level1.reset_state()  
            SCREEN.blit(intro_bg1, (0, 0))
            lines = [
                "The day was cloudy, it would have rained soon.",
                "Suddenly, Muna found herself transported to a realm of demons and monsters.",
                "And she hears a voice in her head, 'You have been chosen.",
                "Find treasure and take it back, enjoy your life!",
                "But first, stop these Bones, let's see if you are truly worthy'"
            ]
            y_offset = 210
            for i, line in enumerate(lines):
                draw_outlined_text(SCREEN, line, intro_font, (SCREEN_WIDTH // 2, y_offset + i * 55), (255, 255, 255), (0, 0, 0))
            draw_outlined_text(SCREEN, "Press Space to start", large_font,
                               (SCREEN_WIDTH // 2, y_offset + len(lines) * 55 + 65), (255, 255, 255), (0, 0, 0))
            pygame.display.update()
            if keys[pygame.K_SPACE]:
                pygame.time.delay(250)
                state = 'level1'
            continue

        if state == 'level1':
            result = level1.draw(SCREEN, keys)
            if result == True:
                pygame.time.delay(500)
                state = 'level1intro2'
            elif result == 'game_over':
                pygame.time.delay(500)
                state = 'start'
            pygame.display.update()
            continue

       
        if state == 'level1intro2':
            SCREEN.blit(intro_bg2, (0, 0))
            lines = [
                "You have been deemed worthy.",
                "Now, find the treasure."
            ]
            y_offset = 340
            for i, line in enumerate(lines):
                draw_outlined_text(SCREEN, line, intro_font, (SCREEN_WIDTH // 2, y_offset + i * 65), (255, 255, 255), (0, 0, 0))
            draw_outlined_text(SCREEN, "Press Space to start.", large_font,
                               (SCREEN_WIDTH // 2, y_offset + len(lines) * 65 + 60), (255, 255, 255), (0, 0, 0))
            pygame.display.update()
            if keys[pygame.K_SPACE]:
                pygame.time.delay(250)
                state = 'level2'
            continue

        if state == 'level2':
            SCREEN.fill((0, 0, 0))
            result = level2.draw(SCREEN, clock)
            if result:
                state = 'level3'
            pygame.display.update()
            continue

    
        if state == 'level3':
            finished = level3.draw()
            if finished:
                state = 'end'
            continue

        if state == 'end':
            pygame.quit()
            break

if __name__ == '__main__':
    main()
