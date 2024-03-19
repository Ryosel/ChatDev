'''
This file contains the settings for the game, such as screen dimensions, colors, and player/zombie attributes.
'''
# Screen dimensions
WIDTH = 800
HEIGHT = 600
# Frames per second
FPS = 60
# Colors
BG_COLOR = (0, 0, 0)  # Black
PLAYER_COLOR = (0, 255, 0)  # Green
ZOMBIE_COLOR = (255, 0, 0)  # Red
# Player settings
PLAYER_SIZE = (50, 50)
PLAYER_SPEED = 5
PLAYER_START_POS = (WIDTH // 2, HEIGHT // 2)
# Zombie settings
ZOMBIE_SIZE = (50, 50)
ZOMBIE_SPEED = 2
ZOMBIE_COUNT = 5