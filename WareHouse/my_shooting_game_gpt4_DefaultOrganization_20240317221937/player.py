'''
This file contains the Player class which handles player movement, shooting, and collision detection.
'''
import pygame
from bullet import Bullet
class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.speed = 5
        self.bullets = []
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.x < 0 or bullet.rect.x > self.screen.get_width() or \
               bullet.rect.y < 0 or bullet.rect.y > self.screen.get_height():
                bullet.alive = False
    def draw(self):
        self.screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw()
    def shoot(self, mouse_pos):
        direction = pygame.math.Vector2(mouse_pos) - self.rect.center
        direction = direction.normalize()
        bullet = Bullet(self.screen, self.rect.center, direction)
        self.bullets.append(bullet)