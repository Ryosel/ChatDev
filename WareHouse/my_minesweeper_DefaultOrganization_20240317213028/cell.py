'''
This file defines the Cell class, which represents each cell on the Minesweeper board.
'''
import pygame
class Cell:
    cell_size = 20
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.adjacent_mines = 0
    def draw(self, surface):
        rect = pygame.Rect(self.x * Cell.cell_size, self.y * Cell.cell_size, Cell.cell_size, Cell.cell_size)
        if self.is_revealed:
            if self.is_mine:
                pygame.draw.rect(surface, (255, 0, 0), rect)
            else:
                pygame.draw.rect(surface, (200,200,200), rect)
                if self.adjacent_mines > 0:
                    font = pygame.font.SysFont(None, 24)
                    text = font.render(str(self.adjacent_mines), True, (0, 0, 0))
                    text_rect = text.get_rect(center=rect.center)
                    surface.blit(text, text_rect)
        else:
            pygame.draw.rect(surface, (100, 100, 100), rect)
            if self.is_flagged:
                pygame.draw.circle(surface, (0, 0, 255), rect.center, Cell.cell_size // 4)
    def reveal(self, board):
        if not self.is_flagged and not self.is_revealed:
            self.is_revealed = True
            if self.is_mine:
                return True  # Game over
            elif self.adjacent_mines == 0:
                # Recursively reveal adjacent cells that are not mines and not flagged
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        x = self.x + dx
                        y = self.y + dy
                        if 0 <= x < board.width and 0 <= y < board.height:
                            neighbor = board.cells[x][y]
                            if not neighbor.is_mine and not neighbor.is_revealed:
                                neighbor.reveal(board)
        return False
    def toggle_flag(self):
        if not self.is_revealed:
            self.is_flagged = not self.is_flagged