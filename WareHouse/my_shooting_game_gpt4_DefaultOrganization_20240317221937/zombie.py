'''
This file contains the Zombie class which represents a zombie enemy that chases the player.
'''
import pygame
class Zombie:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('zombie.png')
        self.rect = self.image.get_rect()
        self.speed = 2
    def update(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed
    def draw(self):
        self.screen.blit(self.image, self.rect)