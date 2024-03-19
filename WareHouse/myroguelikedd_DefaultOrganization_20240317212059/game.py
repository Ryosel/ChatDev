'''
This file contains the Game class.
'''
import pygame
from player import Player
class Game:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Roguelike Game")
        self.player = Player(self.window_width // 2, self.window_height // 2)
        self.running = True
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player.stop_up()
                elif event.key == pygame.K_s:
                    self.player.stop_down()
                elif event.key == pygame.K_a:
                    self.player.stop_left()
                elif event.key == pygame.K_d:
                    self.player.stop_right()
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move_up()
        if keys[pygame.K_s]:
            self.player.move_down()
        if keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_d]:
            self.player.move_right()
        self.player.update()
    def render(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        pygame.display.flip()
    def run(self):
        pygame.init()
        while self.running:
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
# Create and run the game
game = Game(800, 600)
game.run()