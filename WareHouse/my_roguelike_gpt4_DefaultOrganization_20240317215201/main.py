'''
This is the main game file for a top-down 2D roguelike zombie game. It initializes the game, creates a window, and runs the game loop.
'''
import pygame
import sys
from settings import Settings
from player import Player
from zombie import Zombie
class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Zombie Rogue")
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.zombies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self._create_zombies()
    def _create_zombies(self):
        for i in range(self.settings.zombie_count):
            zombie = Zombie(self)
            self.zombies.add(zombie)
            self.all_sprites.add(zombie)
    def run(self):
        while True:
            self._check_events()
            self._update_sprites()
            self._update_screen()
            self.clock.tick(self.settings.fps)
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.player.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.player.check_keyup_events(event)
    def _update_sprites(self):
        self.all_sprites.update()
        if pygame.sprite.spritecollideany(self.player, self.zombies):
            self._end_game()
    def _end_game(self):
        pygame.quit()
        sys.exit()
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
if __name__ == '__main__':
    game = Game()
    game.run()