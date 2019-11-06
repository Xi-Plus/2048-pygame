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
        self.board[a][b] = Block(2, a, b)
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
        score = 0
        for i in range(4):
            j = 0
            while j <= 2:
                if self.board[i][j] and self.board[i][j + 1] and self.board[i][j].val == self.board[i][j + 1].val:
                    self.board[i][j].val *= 2
                    score += self.board[i][j].val
                    for k in range(j + 1, 3):
                        self.board[i][k] = self.board[i][k + 1]
                    self.board[i][3] = None
                    moved = True
                j += 1
        return moved, score

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
        score = 0
        for i in range(4):
            j = 3
            while j >= 1:
                if self.board[i][j] and self.board[i][j - 1] and self.board[i][j].val == self.board[i][j - 1].val:
                    self.board[i][j].val *= 2
                    score += self.board[i][j].val
                    for k in range(j - 1, 0, -1):
                        self.board[i][k] = self.board[i][k - 1]
                    self.board[i][0] = None
                    moved = True
                j -= 1
        return moved, score

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
        score = 0
        for i in range(4):
            j = 0
            while j <= 2:
                if self.board[j][i] and self.board[j + 1][i] and self.board[j][i].val == self.board[j + 1][i].val:
                    self.board[j][i].val *= 2
                    score += self.board[j][i].val
                    for k in range(j + 1, 3):
                        self.board[k][i] = self.board[k + 1][i]
                    self.board[3][i] = None
                    moved = True
                j += 1
        return moved, score

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
        score = 0
        for i in range(4):
            j = 3
            while j >= 1:
                if self.board[j][i] and self.board[j - 1][i] and self.board[j][i].val == self.board[j - 1][i].val:
                    self.board[j][i].val *= 2
                    score += self.board[j][i].val
                    for k in range(j - 1, 0, -1):
                        self.board[k][i] = self.board[k - 1][i]
                    self.board[0][i] = None
                    moved = True
                j -= 1
        return moved, score

    def check_gameover(self):
        if np.sum(self.board == None) != 0:
            return False
        for i in range(4):
            for j in range(3):
                if self.board[i][j] and self.board[i][j] and self.board[i][j].val == self.board[i][j + 1].val:
                    return False
        for i in range(4):
            for j in range(3):
                if self.board[j][i] and self.board[j + 1][i] and self.board[j][i].val == self.board[j + 1][i].val:
                    return False
        return True

    def updatexy(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j]:
                    self.board[i][j].x = i
                    self.board[i][j].y = j

class Block:
    def __init__(self, val, x, y):
        self.val = val
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.val)
