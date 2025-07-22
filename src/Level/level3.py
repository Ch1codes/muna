import pygame
from sys import exit
from random import randint, choice
from ..config.animations import walk_frames

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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk = walk_frames[0][:6]
        self.player_index = 0
        self.player_jump = walk_frames[0][4]
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 850))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('Assets/level3/audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 850:
            self.gravity = -17
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 850:
            self.rect.bottom = 850

    def animation_state(self):
        if self.rect.bottom < 850:
            self.image = self.player_jump
        else:
            self.player_index += 0.18
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def reset(self):
        self.rect.midbottom = (80, 850)
        self.gravity = 0

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        if self.rect.x <= 1350:
            self.rect.x += 1.2

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_1 = pygame.image.load('Assets/level3/graphics/fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('Assets/level3/graphics/fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 720
        else:
            snail_1 = pygame.image.load('Assets/level3/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('Assets/level3/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 850
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(1500, 1600), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

def display_score(start_time):
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    return current_time

def collision_sprite(player, obstacle_group):
    global failed_attempt, game_active
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        player.sprite.reset()
        game_active = False
        failed_attempt = True
        return False
    else:
        return True

def draw():
    global failed_attempt, game_active
    pygame.init()
    screen = pygame.display.set_mode((1400, 900))
    pygame.display.set_caption('Run Muna Run')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('Assets/level3/font/Pixeltype.ttf', 50)

    game_active = False
    failed_attempt = False
    level_completed = False
    score = 0
    start_time = 0

    player = pygame.sprite.GroupSingle()
    player.add(Player())
    obstacle_group = pygame.sprite.Group()

    sky_surface = pygame.image.load('Assets/level3/mountain.png').convert()
    ground_surface = pygame.image.load('Assets/level3/groundblack.png').convert()
    intro_surface = pygame.image.load('Assets/level3/introscreen.png').convert_alpha()
    outro_surface = pygame.image.load('Assets/level3/outroscreen.png').convert_alpha()

    INTRO_TEXT_COLOR = (255, 255, 255)
    INTRO_SHADOW_COLOR = (0, 0, 0)
    OUTRO_TEXT_COLOR = (255, 215, 0)
    OUTRO_SHADOW_COLOR = (0, 0, 0)

    intro_lines = [
        ("Now, the final test remains.", (700, 100)),
        ("Can Muna escape with her fortune?", (700, 150)),
        ("The evil Snails and evil Flies are coming!", (700, 200))
    ]

    try_again_msg = ("TRY AGAIN!", (700, 700))
    press_space_msg = ("Press space to run", (700, 700))

    outro_lines = [
        ("Congratulations!!!", (700, 450)),
        ("Muna has reached safely back to the human realms.", (700, 530)),
        ("Now she can use her riches for good causes.", (700, 580))
    ]

    OBSTACLE_TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(OBSTACLE_TIMER, 1500)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if game_active and not level_completed:
                if event.type == OBSTACLE_TIMER and player.sprite.rect.x <= 1100:
                    obstacle_group.add(Obstacle(choice(['fly', 'fly', 'snail', 'snail', 'snail'])))

            if not game_active and failed_attempt:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    failed_attempt = False
                    obstacle_group.empty()
                    player.sprite.reset()
                    score = 0
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

            if not game_active and not failed_attempt and not level_completed:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    score = 0
                    start_time = int(pygame.time.get_ticks() / 1000)

            if level_completed:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    level_completed = False
                    obstacle_group.empty()
                    player.sprite.reset()
                    score = 0
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

        if not game_active and not failed_attempt and not level_completed:
            # Show intro screen
            screen.blit(intro_surface, (0, 0))
            for text, center in intro_lines:
                draw_outlined_text(screen, text, test_font, center, INTRO_TEXT_COLOR, INTRO_SHADOW_COLOR)
            draw_outlined_text(screen, press_space_msg[0], test_font, press_space_msg[1], INTRO_TEXT_COLOR, INTRO_SHADOW_COLOR)

        elif game_active and not level_completed:
            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 850))
            score = display_score(start_time)
            player.draw(screen)
            player.update()
            obstacle_group.draw(screen)
            obstacle_group.update()
            game_active = collision_sprite(player, obstacle_group)
            if player.sprite.rect.x >= 1300:
                level_completed = True
                game_active = False

        elif level_completed:
            screen.blit(outro_surface, (0, 0))
            box_rect = pygame.Surface((900, 160), pygame.SRCALPHA)
            box_rect.fill((0, 0, 0, 10))
            screen.blit(box_rect, (250, 430))
            for text, center in outro_lines:
                draw_outlined_text(screen, text, test_font, center, OUTRO_TEXT_COLOR, OUTRO_SHADOW_COLOR)

        elif failed_attempt:
            screen.blit(intro_surface, (0, 0))
            for text, center in intro_lines:
                draw_outlined_text(screen, text, test_font, center, INTRO_TEXT_COLOR, INTRO_SHADOW_COLOR)
            draw_outlined_text(screen, try_again_msg[0], test_font, try_again_msg[1], INTRO_TEXT_COLOR, INTRO_SHADOW_COLOR)

        pygame.display.update()
        clock.tick(60)
