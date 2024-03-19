'''
This is the main file for the top-down 2D roguelike game. It includes the Game class, Player class, and the main function to run the game.
The player can move with w, a, s, d to go up, down, left, and right. Diagonal movement has been implemented and normalized, and boundary checking has been optimized.
'''
import pygame
import sys
import math  # Imported math module for accurate square root calculation
# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    def update(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dy -= PLAYER_SPEED
        if keys[pygame.K_s]:
            dy += PLAYER_SPEED
        if keys[pygame.K_a]:
            dx -= PLAYER_SPEED
        if keys[pygame.K_d]:
            dx += PLAYER_SPEED
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            factor = math.sqrt(2)  # Accurate square root calculation
            dx /= factor
            dy /= factor
        # Update rect position
        self.rect.x += dx
        self.rect.y += dy
        # Boundary checking
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Roguelike Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys)
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
def main():
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()