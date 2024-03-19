'''
This file contains settings for the top-down 2D roguelike zombie game.
'''
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (50, 50, 50)
        self.player_speed = 5
        self.zombie_speed = 2
        self.zombie_count = 5
        self.fps = 60