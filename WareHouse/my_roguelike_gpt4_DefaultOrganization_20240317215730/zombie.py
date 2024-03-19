'''
This file defines the Zombie class, its initialization, AI for chasing the player, and rendering.
'''
import pygame
import settings
from random import randint
class Zombie:
    def __init__(self, game):
        self.game = game
        self.x, self.y = (randint(0, settings.WIDTH), randint(0, settings.HEIGHT))
        self.width, self.height = settings.ZOMBIE_SIZE
        self.color = settings.ZOMBIE_COLOR
        self.speed = settings.ZOMBIE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        if self.x < self.game.player.x:
            self.x += self.speed
        elif self.x > self.game.player.x:
            self.x -= self.speed
        if self.y < self.game.player.y:
            self.y += self.speed
        elif self.y > self.game.player.y:
            self.y -= self.speed
        self.rect.topleft = (self.x, self.y)
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    def collides_with(self, player):
        return self.rect.colliderect(player.rect)