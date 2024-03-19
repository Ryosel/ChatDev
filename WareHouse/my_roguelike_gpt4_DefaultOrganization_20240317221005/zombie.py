'''
This file defines the Zombie class for the top-down 2D roguelike zombie game.
'''
import pygame
# Constants
ZOMBIE_COLOR = (255, 0, 0)
ZOMBIE_SIZE = 50
class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.rect = pygame.Rect(x, y, ZOMBIE_SIZE, ZOMBIE_SIZE)
    def update(self, player, obstacles):
        # Calculate direction vector (dx, dy) towards the player
        dx, dy = player.x - self.x, player.y - self.y
        dist = (dx**2 + dy**2)**0.5  # Distance to the player
        # Normalize the direction vector (unit vector)
        if dist > 0:
            dx, dy = dx / dist, dy / dist
        # Move the zombie towards the player
        self.x += self.speed * dx
        self.y += self.speed * dy
        # Update the zombie's rect position
        self.rect.topleft = (self.x, self.y)
        # Check collision with obstacles after the move
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                # Move back if collided with an obstacle
                self.x -= self.speed * dx
                self.y -= self.speed * dy
                break
        # Update the rect again after checking for collisions
        self.rect.topleft = (self.x, self.y)
    def collides_with(self, player):
        return self.rect.colliderect(player.rect)
    def draw(self, screen):
        pygame.draw.rect(screen, ZOMBIE_COLOR, self.rect)