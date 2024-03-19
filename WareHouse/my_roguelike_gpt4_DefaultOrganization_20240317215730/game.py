'''
This file contains the Game class that manages the game state, including initialization, the game loop, and event handling.
'''
import pygame
import player
import zombie
import settings
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = player.Player(self)
        self.zombies = [zombie.Zombie(self) for _ in range(settings.ZOMBIE_COUNT)]
    def run(self):
        while self.running:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        self.player.update()
        for z in self.zombies:
            z.update()
            if z.collides_with(self.player):
                self.running = False
    def draw(self):
        self.screen.fill(settings.BG_COLOR)
        self.player.draw(self.screen)
        for z in self.zombies:
            z.draw(self.screen)
        pygame.display.flip()