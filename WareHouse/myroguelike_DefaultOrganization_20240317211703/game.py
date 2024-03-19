'''
This file contains the Game class that manages the game logic.
'''
import pygame
class Game:
    def __init__(self):
        self.running = False
        self.display_width = 800
        self.display_height = 600
        self.player_x = self.display_width // 2
        self.player_y = self.display_height // 2
        self.player_speed = 5
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Roguelike Game")
    def run(self):
        pygame.init()
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_y -= self.player_speed
        if keys[pygame.K_s]:
            self.player_y += self.player_speed
        if keys[pygame.K_a]:
            self.player_x -= self.player_speed
        if keys[pygame.K_d]:
            self.player_x += self.player_speed
    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.player_x, self.player_y, 20, 20))
        pygame.display.flip()