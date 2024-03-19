'''
This file defines the Obstacle class for the top-down 2D roguelike zombie game.
'''
import pygame
# Constants
OBSTACLE_COLOR = (128, 128, 128)
OBSTACLE_SIZE = 50
class Obstacle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, OBSTACLE_SIZE, OBSTACLE_SIZE)
    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)