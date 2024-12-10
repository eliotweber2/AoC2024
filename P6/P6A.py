import numpy as np
from copy import deepcopy

with open('./Input6.txt', 'r') as file:
    real = file.read()

example = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

class Guard:
    def __init__(self,board):
        self.board = board
        self.pos = [np.where(board=='^')[0][0],np.where(board=='^')[1][0]]
        self.move = [-1,0]

    def rotate(self):
        if np.array_equal(self.move,[-1,0]):
            self.move = [0,1]
        elif np.array_equal(self.move,[0,1]):
            self.move = [1,0]
        elif np.array_equal(self.move,[1,0]):
            self.move = [0,-1]
        elif np.array_equal(self.move,[0,-1]):
            self.move = [-1,0]

    def tryMove(self):
        self.board[self.pos[0],self.pos[1]] = 'X'
        tempR = self.pos[0] + self.move[0]
        tempC = self.pos[1] + self.move[1]
        if tempR < 0 or tempR >= self.board.shape[0] or tempC < 0 or tempC >= self.board.shape[0]:
            return -1
        if self.board[tempR,tempC] == '#':
            self.rotate()
            return 0
        else:
            self.pos = [tempR,tempC]
            return 1

def format(strBoard):
    rows = strBoard.split('\n')
    return np.array([list(row) for row in rows])

def runGame(board):
    guard = Guard(board)
    while True:
        if (result := guard.tryMove()) == -1:
            return np.where(board=='X')[0].shape[0]

test = format(example)
freal = format(real)
print(runGame(freal))