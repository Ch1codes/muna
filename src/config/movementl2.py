import pygame
from .animationsl2 import idle, walk  # Ensure these are valid lists of animation frames

class Character_state(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.direction = direction
        self.frame_type = idle[direction]

        self.image = self.frame_type.animate(0)
        self.rect = self.image.get_rect(center=(x, y + 20))  # visual sprite rect

        self.speed = 5

        # Feet rect: small collision box at bottom center of the sprite
        feet_width = self.rect.width // 2
        feet_height = 10  # Height of the feet box
        self.feet_rect = pygame.Rect(0, 0, feet_width, feet_height)
        self.update_feet_position()

    def update_feet_position(self):
        """Place feet_rect at the bottom center of the sprite."""
        self.feet_rect.midbottom = self.rect.midbottom

    def character_movement(self, keys, wall_rects):
        dx = dy = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction = 0
            self.frame_type = walk[self.direction]
            dx = self.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction = 1
            self.frame_type = walk[self.direction]
            dx = -self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction = 2
            self.frame_type = walk[self.direction]
            dy = self.speed
        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction = 3
            self.frame_type = walk[self.direction]
            dy = -self.speed
        else:
            self.frame_type = idle[self.direction]

        # --- Move feet rect first ---
        self.feet_rect.x += dx
        for wall in wall_rects:
            if self.feet_rect.colliderect(wall):
                if dx > 0:
                    self.feet_rect.right = wall.left
                elif dx < 0:
                    self.feet_rect.left = wall.right

        self.feet_rect.y += dy
        for wall in wall_rects:
            if self.feet_rect.colliderect(wall):
                if dy > 0:
                    self.feet_rect.bottom = wall.top
                elif dy < 0:
                    self.feet_rect.top = wall.bottom

        # --- Now move the sprite to match the feet position ---
        self.rect.midbottom = self.feet_rect.midbottom

    def update(self, frame_timer):
        self.image = self.frame_type.animate(frame_timer)
        self.update_feet_position()

