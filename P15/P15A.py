import numpy as np

example_board = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########'''

example_moves = '''<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

with open('Input15.txt') as f:
    inp = f.read()
    board_r = inp.split('\n\n')[0]
    moves_r = inp.split('\n\n')[1]

def parse(board):
    return np.array([[cell for cell in row] for row in board.split('\n')])

def get_init_pos(board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i,j] == '@':
                return [i,j]

def can_push(dir,coords,board,type='O'):
    new_coords = [coords[0]+dir[0],coords[1]+dir[1]]
    if board[new_coords[0],new_coords[1]] == '.':
        if board[coords[0],coords[1]] == 'O':
            board[coords[0],coords[1]] = '.'
            board[new_coords[0],new_coords[1]] = type
        return True
    elif board[new_coords[0],new_coords[1]] == 'O':
        r = can_push(dir,new_coords,board)
        if r:
            board[coords[0],coords[1]] = '.'
            board[new_coords[0],new_coords[1]] = type
        return r
    else:
        return False
    
def move(coords,dir_s):
    dir = [0,0]
    if dir_s == '^':
        dir = [-1,0]
    elif dir_s == 'v':
        dir = [1,0]
    elif dir_s == '<':
        dir = [0,-1]
    elif dir_s == '>':
        dir = [0,1]

    if can_push(dir,coords,board,type='.'):
        #board[coords[0],coords[1]] = '.'
        #board[coords[0]+dir[0],coords[1]+dir[1]] = 'O'
        return [coords[0]+dir[0],coords[1]+dir[1]]
    else:
        return coords
    
def score(board):
    tot = 0
    for r in range(board.shape[0]):
        for c in range(board.shape[1]):
            if board[r,c] == 'O':
                tot += 100*r+c
    
    return tot

board = parse(board_r)
pos = get_init_pos(board)
moves = [x for x in moves_r if x != '\n']
board[pos[0],pos[1]] = '.'
steps = len(moves)
for i in range(steps):
    pos = move(pos,moves[i])
    #print(i,pos)
    #print(board)

#print(board)
print(score(board))