'''
This file defines the Board class, which handles the logic and rendering of the Minesweeper board.
'''
import pygame
import random
from cell import Cell
class Board:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.cells = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.populate_mines()
    def populate_mines(self):
        mine_positions = set()
        while len(mine_positions) < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in mine_positions:
                mine_positions.add((x, y))
                self.cells[x][y].is_mine = True
        for x in range(self.width):
            for y in range(self.height):
                if self.cells[x][y].is_mine:
                    continue
                count = sum((self.cells[i][j].is_mine for i in range(max(0, x-1), min(self.width, x+2))
                             for j in range(max(0, y-1), min(self.height, y+2)) if (i, j) != (x, y)))
                self.cells[x][y].adjacent_mines = count
    def handle_click(self, position, button):
        x, y = position[0] // Cell.cell_size, position[1] // Cell.cell_size
        if 0 <= x < self.width and 0 <= y < self.height:  # Check if the click is within the board
            if button == 1:  # Left click
                if self.cells[x][y].reveal(self):
                    return True  # Game over
            elif button == 3:  # Right click
                self.cells[x][y].toggle_flag()
        return False
    def draw(self, surface):
        for row in self.cells:
            for cell in row:
                cell.draw(surface)