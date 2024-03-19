'''
This file contains the Player class.
'''
import pygame
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.width = 32
        self.height = 32
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    def move_up(self):
        self.moving_up = True
    def move_down(self):
        self.moving_down = True
    def move_left(self):
        self.moving_left = True
    def move_right(self):
        self.moving_right = True
    def stop_up(self):
        self.moving_up = False
    def stop_down(self):
        self.moving_down = False
    def stop_left(self):
        self.moving_left = False
    def stop_right(self):
        self.moving_right = False
    def update(self):
        if self.moving_up:
            self.y -= self.speed
        if self.moving_down:
            self.y += self.speed
        if self.moving_left:
            self.x -= self.speed
        if self.moving_right:
            self.x += self.speed
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))