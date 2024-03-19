'''
This is the main file of the simple run game application.
'''
import tkinter as tk
from game import Game
class SimpleRunGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Run Game")
        self.game = Game(self.master)  # Pass the master window to the Game class
        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="white")
        self.canvas.pack()
        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()
        self.update()
    def on_key_press(self, event):
        self.game.handle_key_press(event.keysym)
    def update(self):
        if not self.game.is_game_over():  # Check if the game is over
            self.game.update()
            self.canvas.delete("all")
            self.game.draw(self.canvas)
        self.master.after(20, self.update)
def main():
    root = tk.Tk()
    app = SimpleRunGameApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()