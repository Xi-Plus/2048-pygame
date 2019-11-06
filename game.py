import random
import numpy as np


class Game:
    def __init__(self):
        self.board = np.full((4, 4), None)
        self.score = 0

    def random_lay(self):
        print(np.sum(self.board == None))
        if np.sum(self.board == None) == 0:
            print('no place to lay')
            return -1, -1

        a = random.randint(0, 3)
        b = random.randint(0, 3)
        while self.board[a][b] is not None:
            a = random.randint(0, 3)
            b = random.randint(0, 3)
        self.board[a][b] = Block(a, b, 2)
        return a, b

    def move_left(self):
        print('left')
        moved = False
        for i in range(4):
            for j in range(3):
                for k in range(3):
                    if self.board[i][k] is None and self.board[i][k + 1] is not None:
                        self.board[i][k] = self.board[i][k + 1]
                        self.board[i][k + 1] = None
                        moved = True
        return moved

    def move_right(self):
        print('right')
        moved = False
        for i in range(4):
            for j in range(3):
                for k in range(3, 0, -1):
                    if self.board[i][k] is None and self.board[i][k - 1] is not None:
                        self.board[i][k] = self.board[i][k - 1]
                        self.board[i][k - 1] = None
                        moved = True
        return moved

    def move_up(self):
        print('up')
        moved = False
        for i in range(4):
            for j in range(3):
                for k in range(3):
                    if self.board[k][i] is None and self.board[k + 1][i] is not None:
                        self.board[k][i] = self.board[k + 1][i]
                        self.board[k + 1][i] = None
                        moved = True
        return moved

    def move_down(self):
        print('down')
        moved = False
        for i in range(4):
            for j in range(3):
                for k in range(3, 0, -1):
                    if self.board[k][i] is None and self.board[k - 1][i] is not None:
                        self.board[k][i] = self.board[k - 1][i]
                        self.board[k - 1][i] = None
                        moved = True
        return moved


class Block:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __repr__(self):
        return str(self.val)
