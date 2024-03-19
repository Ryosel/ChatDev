'''
This file contains the Obstacle class which represents the obstacles in the game.
'''
import tkinter as tk
from game import Game
class Obstacle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.obstacle_image = tk.PhotoImage(file="obstacle.png")
        self.obstacle_id = self.canvas.create_image(800, 300, image=self.obstacle_image)