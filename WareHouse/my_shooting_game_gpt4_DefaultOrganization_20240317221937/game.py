'''
This file contains the Game class which is responsible for initializing the game, running the game loop, and handling events.
'''
import pygame
from player import Player
from zombie import Zombie
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen)
        self.zombies = [Zombie(self.screen) for _ in range(5)]
        self.running = True
    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                    self.player.shoot(pygame.mouse.get_pos())
            self.player.update()
            for bullet in self.player.bullets[:]:
                if not bullet.alive:
                    self.player.bullets.remove(bullet)
            player_collided = False
            for zombie in self.zombies:
                zombie.update(self.player)
                if zombie.rect.colliderect(self.player.rect):
                    player_collided = True
                    break  # Exit the loop as the game should end
            if player_collided:
                self.running = False  # End the game outside of the zombie update loop
            for bullet in self.player.bullets[:]:  # Iterate over a copy of the bullets list
                for zombie in self.zombies[:]:  # Iterate over a copy of the zombies list
                    if bullet.rect.colliderect(zombie.rect):
                        self.player.bullets.remove(bullet)
                        self.zombies.remove(zombie)
                        break  # Break to avoid a RuntimeError after removing the bullet
            self.screen.fill((0, 0, 0))
            self.player.draw()
            for zombie in self.zombies:
                zombie.draw()
            pygame.display.flip()
        pygame.quit()