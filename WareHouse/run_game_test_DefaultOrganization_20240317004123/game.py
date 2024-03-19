'''
This file contains the Game class which represents the game logic.
'''
class Game:
    def __init__(self, master):
        self.master = master
        self.player_x = 400
        self.player_y = 500
    def handle_key_press(self, key):
        if key == "Left":
            self.player_x -= 10
        elif key == "Right":
            self.player_x += 10
    def update(self):
        self.player_y -= 5  # Move the player upwards by 5 units in each update
    def draw(self, canvas):
        canvas.create_rectangle(self.player_x - 20, self.player_y - 20, self.player_x + 20, self.player_y + 20, fill="blue")
    def is_game_over(self):
        return self.player_y <= 0  # Check if the player has reached the top of the canvas