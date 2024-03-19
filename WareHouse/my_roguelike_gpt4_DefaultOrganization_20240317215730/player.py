'''
This file defines the Player class, its initialization, movement, and rendering.
'''
import pygame
import settings
class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = settings.PLAYER_START_POS
        self.width, self.height = settings.PLAYER_SIZE
        self.color = settings.PLAYER_COLOR
        self.speed = settings.PLAYER_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        self.rect.topleft = (self.x, self.y)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)