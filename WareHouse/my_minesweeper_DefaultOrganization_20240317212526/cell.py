'''
This file contains the Cell class which represents a single cell on the game board.
'''
import pygame
class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.revealed = False
    def reveal(self):
        self.revealed = True
    def draw(self, screen):
        if self.revealed:
            pygame.draw.rect(screen, (200, 200, 200), (self.x * self.size, self.y * self.size, self.size, self.size))
        else:
            pygame.draw.rect(screen, (100, 100, 100), (self.x * self.size, self.y * self.size, self.size, self.size))