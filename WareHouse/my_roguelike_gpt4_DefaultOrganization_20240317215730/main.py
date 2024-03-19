'''
This is the entry point of the top-down 2D roguelike zombie game. It initializes the game and starts the main loop.
'''
import pygame
import game
def main():
    pygame.init()
    game_instance = game.Game()
    game_instance.run()
if __name__ == "__main__":
    main()