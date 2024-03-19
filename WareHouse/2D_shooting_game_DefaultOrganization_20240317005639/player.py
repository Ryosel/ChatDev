'''
This file contains the Player class which represents the player character.
'''
import pygame
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        # Add diagonal movement logic
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            self.x -= self.speed
            self.y -= self.speed
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.x -= self.speed
            self.y += self.speed
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            self.x += self.speed
            self.y -= self.speed
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            self.x += self.speed
            self.y += self.speed
        self.rect.center = (self.x, self.y)
    def render(self, screen):
        screen.blit(self.image, self.rect)