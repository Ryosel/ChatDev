'''
This file defines the Player class for the top-down 2D roguelike zombie game.
'''
import pygame
# Constants
PLAYER_COLOR = (0, 255, 0)
PLAYER_SIZE = 50
class Player:
    def __init__(self, x, y, screen_width, screen_height):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = 5
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y = max(0, self.y - self.speed)
        if keys[pygame.K_s]:
            self.y = min(self.screen_height - self.rect.height, self.y + self.speed)
        if keys[pygame.K_a]:
            self.x = max(0, self.x - self.speed)
        if keys[pygame.K_d]:
            self.x = min(self.screen_width - self.rect.width, self.x + self.speed)
        self.rect.topleft = (self.x, self.y)
    def update(self):
        pass  # For now, the player does not have any other updates to process
    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)