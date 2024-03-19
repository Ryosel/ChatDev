'''
This is the main file for the Minesweeper game. It initializes the game and starts the Pygame loop.
'''
import pygame
from game import Game
def main():
    pygame.init()
    minesweeper_game = Game()
    minesweeper_game.run()
    pygame.quit()
if __name__ == "__main__":
    main()