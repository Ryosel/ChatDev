'''
This file contains the Game class which manages the game loop and game state.
'''
import pygame
from player import Player
class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2D Shooting Game")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.player = Player(self.screen_width // 2, self.screen_height // 2)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
    def update(self):
        self.player.update()
    def render(self):
        self.screen.fill((0, 0, 0))
        self.player.render(self.screen)
        pygame.display.flip()
    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)