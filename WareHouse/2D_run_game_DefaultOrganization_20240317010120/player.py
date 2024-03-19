'''
This file contains the Player class which represents the player character in the game.
'''
import tkinter as tk
from game import Game
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.player_image = tk.PhotoImage(file="player.png")
        self.player_id = self.canvas.create_image(100, 300, image=self.player_image)
    def move(self, dx, dy):
        self.canvas.move(self.player_id, dx, dy)