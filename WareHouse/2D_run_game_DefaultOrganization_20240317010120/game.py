'''
This file contains the Game class which manages the game logic and GUI.
'''
import tkinter as tk
from player import Player
from obstacle import Obstacle
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.scroll_speed = 5
        self.scroll_position = 0
        self.player = Player(self.canvas)
        self.obstacles = []
        self.create_obstacles()
    def start(self):
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.handle_keypress)
        self.update()
    def create_obstacles(self):
        # Code to create obstacles
        for i in range(5):
            obstacle = Obstacle(self.canvas)
            self.obstacles.append(obstacle)
    def update(self):
        self.scroll_position += self.scroll_speed
        self.canvas.move("obstacle", -self.scroll_speed, 0)
        self.check_collision()
        self.canvas.after(20, self.update)
    def handle_keypress(self, event):
        # Code to handle keypress events
        if event.keysym == "Up":
            self.player.move(0, -10)
        elif event.keysym == "Down":
            self.player.move(0, 10)
        elif event.keysym == "Left":
            self.player.move(-10, 0)
        elif event.keysym == "Right":
            self.player.move(10, 0)
    def check_collision(self):
        # Code to check collision between player and obstacles
        player_coords = self.canvas.coords(self.player.player_id)
        for obstacle in self.obstacles:
            obstacle_coords = self.canvas.coords(obstacle.obstacle_id)
            if self.is_collision(player_coords, obstacle_coords):
                print("Collision!")
    def is_collision(self, coords1, coords2):
        x1, y1, x2, y2 = coords1
        x3, y3, x4, y4 = coords2
        if (x1 < x4 and x2 > x3) and (y1 < y4 and y2 > y3):
            return True
        return False
class Obstacle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.obstacle_image = tk.PhotoImage(file="obstacle.png")
        self.obstacle_id = self.canvas.create_image(800, 300, image=self.obstacle_image)
class Player:
    def __init__(self, canvas):
        self.canvas = canvas
        self.player_image = tk.PhotoImage(file="player.png")
        self.player_id = self.canvas.create_image(100, 300, image=self.player_image)
    def move(self, dx, dy):
        self.canvas.move(self.player_id, dx, dy)