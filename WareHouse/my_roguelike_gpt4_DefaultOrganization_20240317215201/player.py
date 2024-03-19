'''
Defines the Player class for the top-down 2D roguelike zombie game.
'''
import pygame
from settings import Settings
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.y += self.settings.player_speed
        self.rect.x = self.x
        self.rect.y = self.y
    def check_keydown_events(self, event):
        if event.key == pygame.K_d:
            self.moving_right = True
        elif event.key == pygame.K_a:
            self.moving_left = True
        elif event.key == pygame.K_w:
            self.moving_up = True
        elif event.key == pygame.K_s:
            self.moving_down = True
    def check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.moving_right = False
        elif event.key == pygame.K_a:
            self.moving_left = False
        elif event.key == pygame.K_w:
            self.moving_up = False
        elif event.key == pygame.K_s:
            self.moving_down = False