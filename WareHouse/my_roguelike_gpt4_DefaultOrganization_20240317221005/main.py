'''
This is the main file for the top-down 2D roguelike zombie game. It initializes the game and starts the main loop.
'''
import pygame
import sys
import random
from player import Player
from zombie import Zombie
from obstacle import Obstacle
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (50, 50, 50)
FPS = 60
NUMBER_OF_ZOMBIES = 5
NUMBER_OF_OBSTACLES = 10
SPAWN_ZOMBIE_EVERY = 5000  # milliseconds
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Zombie Chase Game')
        self.clock = pygame.time.Clock()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.zombies = [Zombie(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(NUMBER_OF_ZOMBIES)]
        self.obstacles = [Obstacle(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(NUMBER_OF_OBSTACLES)]
        self.running = True
        self.last_spawn_time = pygame.time.get_ticks()
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            current_time = pygame.time.get_ticks()
            if current_time - self.last_spawn_time > SPAWN_ZOMBIE_EVERY:
                self.zombies.append(Zombie(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))
                self.last_spawn_time = current_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.player.handle_keys()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()
    def update(self):
        self.player.update()
        for zombie in self.zombies:
            zombie.update(self.player, self.obstacles)
            if zombie.collides_with(self.player):
                self.running = False
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.player.draw(self.screen)
        for zombie in self.zombies:
            zombie.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        pygame.display.flip()
def main():
    game = Game()
    game.run()
if __name__ == '__main__':
    main()