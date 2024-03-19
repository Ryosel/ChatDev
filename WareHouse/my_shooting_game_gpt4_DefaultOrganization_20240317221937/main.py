'''
This is the main file for the top-down 2D roguelike shooting zombie game. It initializes the game and starts the main loop.
'''
import pygame
import sys
from game import Game
def main():
    pygame.init()
    game = Game()
    game.run()
if __name__ == "__main__":
    main()