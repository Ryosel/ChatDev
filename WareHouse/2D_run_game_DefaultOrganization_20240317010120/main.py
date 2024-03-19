'''
This is the main file of the 2D run game with scroll view application.
'''
import tkinter as tk
from game import Game
def main():
    root = tk.Tk()
    root.title("2D Run Game")
    game = Game(root)
    game.start()
    root.mainloop()
if __name__ == "__main__":
    main()