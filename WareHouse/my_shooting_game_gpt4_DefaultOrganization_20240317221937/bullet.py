'''
This file contains the Bullet class which represents a bullet shot by the player.
'''
import pygame
class Bullet:
    def __init__(self, screen, position, direction):
        self.screen = screen
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect(center=position)
        self.speed = 10
        self.direction = direction
        self.alive = True
    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
    def draw(self):
        self.screen.blit(self.image, self.rect)