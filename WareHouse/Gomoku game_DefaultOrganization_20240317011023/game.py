'''
This file contains the Game class which represents the Gomoku game logic.
'''
class Game:
    def __init__(self):
        self.board_size = 15
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'
    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            return True
        return False
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 5):
                new_row = row + dx * i
                new_col = col + dy * i
                if 0 <= new_row < self.board_size and 0 <= new_col < self.board_size:
                    if self.board[new_row][new_col] == self.current_player:
                        count += 1
                    else:
                        break
                else:
                    break
            if count == 5:
                return True
        return False
    def reset(self):
        self.board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.current_player = 'X'