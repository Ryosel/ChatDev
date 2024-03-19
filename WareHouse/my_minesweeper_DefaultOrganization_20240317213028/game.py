'''
This file defines the Game class, which is responsible for initializing the game window,
handling events, and managing the game loop.
'''
import pygame
from board import Board
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.game_screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Minesweeper')
        self.clock = pygame.time.Clock()
        self.board = Board(10, 10, 20)  # Example configuration: 10x10 board with 20 mines
        self.game_over = False
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    self.game_over = self.board.handle_click(event.pos, event.button)
            self.game_screen.fill((255, 255, 255))  # Fill the screen with a white background
            self.board.draw(self.game_screen)
            pygame.display.flip()
            self.clock.tick(30)  # Limit the frame rate to 30 FPS