'''
This is the main file for the Gomoku game.
'''
import tkinter as tk
import tkinter.messagebox as messagebox
from game import Game
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.game = Game()
        self.board_size = 15
        self.cell_size = 40
        self.canvas_size = self.board_size * self.cell_size
        self.canvas = tk.Canvas(self.master, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        for i in range(self.board_size):
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_size)
            self.canvas.create_line(0, i * self.cell_size, self.canvas_size, i * self.cell_size)
    def on_click(self, event):
        row = event.y // self.cell_size
        col = event.x // self.cell_size
        if self.game.make_move(row, col):
            self.draw_piece(row, col, self.game.current_player)
            if self.game.check_winner(row, col):
                self.show_winner_message()
            else:
                self.game.switch_player()
    def draw_piece(self, row, col, player):
        x = col * self.cell_size
        y = row * self.cell_size
        if player == 1:
            self.canvas.create_oval(x, y, x + self.cell_size, y + self.cell_size, fill="black")
        else:
            self.canvas.create_oval(x, y, x + self.cell_size, y + self.cell_size, fill="white")
    def show_winner_message(self):
        winner = "Black" if self.game.current_player == 1 else "White"
        messagebox.showinfo("Game Over", f"{winner} wins!")
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gomoku")
    gomoku_gui = GomokuGUI(root)
    root.mainloop()