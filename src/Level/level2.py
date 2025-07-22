import pygame
from ..config.movementl2 import Character_state
from ..config.map_sketch import map_level2
from sys import exit

pygame.init()

# Constants
tile_size = 50
screen_width = 1400
screen_height = 900
fps = 60

# Tree Class
class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('img/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/GRASS/key.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=(x, y))

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/GRASS/CHEST.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=(x, y))

# Button Class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, SCREEN):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        SCREEN.blit(self.image, self.rect)
        return action

# Exit sprite class
class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# World Class
class World():
    def __init__(self, data):
        self.data = data
        self.key_group = pygame.sprite.Group()
        self.chest_group = pygame.sprite.Group()
        self.wall_rects = []

        self.dirt_img = pygame.transform.scale(pygame.image.load('img/GRASS/Temple_Wall.png'), (tile_size, tile_size))
        self.grass_img = pygame.transform.scale(pygame.image.load('img/GRASS/Temple_Tile.png'), (tile_size, tile_size))
        map_width = len(data[0]) * tile_size
        map_height = len(data) * tile_size
        self.map_surface = pygame.Surface((map_width, map_height)).convert()
        for row_index, row in enumerate(data):
            for col_index, tile in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if tile == 1:
                    self.map_surface.blit(self.dirt_img, (x, y))
                    self.wall_rects.append(pygame.Rect(x, y, tile_size, tile_size))
                elif tile == 2 or tile == 3 or tile == 4:
                    self.map_surface.blit(self.grass_img, (x, y))
                if tile == 3:
                    key = Key(x, y)
                    self.key_group.add(key)
                elif tile == 4:
                    chest = Chest(x, y)
                    self.chest_group.add(chest)

    def draw(self, offset, SCREEN):
        view_rect = pygame.Rect(int(offset.x), int(offset.y), screen_width, screen_height)
        SCREEN.blit(self.map_surface, (0, 0), area=view_rect)
        for key in self.key_group:
            if SCREEN.get_rect().colliderect(key.rect.move(-offset.x, -offset.y)):
                SCREEN.blit(key.image, key.rect.topleft - offset)
        for chest in self.chest_group:
            if SCREEN.get_rect().colliderect(chest.rect.move(-offset.x, -offset.y)):
                SCREEN.blit(chest.image, chest.rect.topleft - offset)

# Camera Group
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_width() // 2
        self.half_h = self.display_surface.get_height() // 2

    def center_target(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player, world, SCREEN):
        self.center_target(player)
        world.draw(self.offset, SCREEN)
        for sprite in sorted(self.sprites(), key=lambda s: s.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

# Main Game Loop - Auto Start
def draw(SCREEN, clock):
    test_font = pygame.font.Font('text/Pixeltype.ttf', 100)
    # key_count=test_font.render(f"Key count: {key}", False, 'RED').convert()
    key = 0
    frame_timer = 0
    world = World(map_level2)
    camera_group = CameraGroup()
    character_state = Character_state(tile_size * 2, tile_size * (len(map_level2) - 1), 3)
    camera_group.add(character_state)
    run = True
    while run:
        clock.tick(fps)
        keys = pygame.key.get_pressed()
        character_state.character_movement(keys, world.wall_rects)
        collected_keys = pygame.sprite.spritecollide(character_state, world.key_group, True)
        if collected_keys:
            key += len(collected_keys)
            print("key collected")
        if key >= 3:
            collected_chests = pygame.sprite.spritecollide(character_state, world.chest_group, True)
            if collected_chests:
                print("Chest collected!")
                return True
        frame_timer = (frame_timer + 1) % fps
        camera_group.update(frame_timer)
        SCREEN.fill((0, 0, 0))
        camera_group.custom_draw(character_state, world, SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_count_text = test_font.render(f"Key count: {key}", False, 'RED')
        SCREEN.blit(key_count_text, (10, 10))
        pygame.display.update()
    pygame.quit()
    exit()

# Run the game
if __name__ == "__main__":
    draw()
