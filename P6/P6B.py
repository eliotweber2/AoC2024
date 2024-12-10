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
    def __init__(self,board,freeStart):
        self.board = board
        self.pos = [np.where(board=='^')[0][0],np.where(board=='^')[1][0]]
        if freeStart:
            self.board[self.pos[0],self.pos[1]] = '.'
        else:
            self.board[self.pos[0],self.pos[1]] = '#'
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

def runGame(board,freeStart):
    guard = Guard(board,freeStart)
    posLst = [[guard.pos,guard.move]]
    while True:
        if (result := guard.tryMove()) == -1:
            return False
        elif result == 1:
            if [guard.pos,guard.move] in posLst:
                return True
            posLst.append([guard.pos,guard.move])

def genGame(board):
    guard = Guard(board,True)
    while True:
        if (result := guard.tryMove()) == -1:
            print(board)
            yield ['_',True]
        elif result == 1:
            yield [guard.pos,False]

def runAll(board):
        correct = []
        default = genGame(deepcopy(board))
        while not (input := next(default))[1]:
            newBoard = deepcopy(board)
            freeStart = True
            if board[input[0][0],input[0][1]] == '^':
                freeStart = False
            else:
                newBoard[input[0][0],input[0][1]] = '#'
            if runGame(newBoard,freeStart):
                if input[0] not in correct:
                    correct.append(input[0])
                    print(input[0])
        return len(correct)

test = format(example)
freal = format(real)
print(runAll(freal))