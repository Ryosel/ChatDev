'''
This is the main file of the Gomoku game.
'''
import tkinter as tk
from game import Game
class GomokuApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku")
        self.game = Game()
        self.create_board()
    def create_board(self):
        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()
        self.buttons = []
        for row in range(self.game.board_size):
            row_buttons = []
            for col in range(self.game.board_size):
                button = tk.Button(self.board_frame, width=4, height=2, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
    def make_move(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.current_player)
            if self.game.check_winner(row, col):
                self.show_winner()
            else:
                self.game.switch_player()
    def show_winner(self):
        winner = self.game.current_player
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_board()
    def reset_board(self):
        self.game.reset()
        for row in range(self.game.board_size):
            for col in range(self.game.board_size):
                self.buttons[row][col].config(text="")
if __name__ == "__main__":
    root = tk.Tk()
    app = GomokuApp(root)
    root.mainloop()