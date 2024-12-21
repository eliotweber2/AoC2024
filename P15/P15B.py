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
    temp = np.array([[cell for cell in row] for row in board.split('\n')])
    board = np.zeros((temp.shape[0],temp.shape[1]*2))
    id = 1
    pos = [0,0]
    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):
            if temp[i,j] == '#':
                board[i,j*2] = -1
                board[i,j*2+1] = -1
            elif temp[i,j] == 'O':
                board[i,j*2] = id
                board[i,j*2+1] = id
                id += 1
            elif temp[i,j] == '@':
                board[i,j*2] = 0
                board[i,j*2+1] = 0
                pos = [i,j*2]
            elif temp[i,j] == '.':
                board[i,j*2] = 0
                board[i,j*2+1] = 0
    return board,pos,id

def can_push(dir,coords,board,other_checked=False):
    if board[coords[0],coords[1]] == 0:
        return True
    elif board[coords[0],coords[1]] == -1:
        return False
    else:
        id = board[coords[0],coords[1]]
        complete = list(zip(*[x for x in np.where(board == id)]))
        complete = [[int(y) for y in x] for x in complete]
        other = [x for x in complete if x != coords][0]
        check = [coords[0]+dir[0],coords[1]+dir[1]]
        if check == other:
            r = can_push(dir,other,board)
            return r
        if [coords[0]-dir[0],coords[1]-dir[1]] == other:
            r = can_push(dir,check,board)
            return r
        r = None
        if other_checked:
            r = can_push(dir,check,board)
        else:
            r = can_push(dir,other,board,True) and can_push(dir,check,board)
        return r
    
def push(dir,coords,board,other_checked=False):
    if board[coords[0],coords[1]] == 0 or board[coords[0],coords[1]] == -1:
        return
    else:
        id = board[coords[0],coords[1]]
        complete = list(zip(*[x for x in np.where(board == id)]))
        complete = [[int(y) for y in x] for x in complete]
        other = [x for x in complete if x != coords][0]
        check = [coords[0]+dir[0],coords[1]+dir[1]]
        if check == other:
            push(dir,other,board)
            board[check[0],check[1]] = board[coords[0],coords[1]]
            board[coords[0],coords[1]] = 0
            return
        if [coords[0]-dir[0],coords[1]-dir[1]] == other:
            push(dir,check,board)
            board[check[0],check[1]] = board[coords[0],coords[1]]
            board[coords[0],coords[1]] = 0
            return
        if other_checked:
            push(dir,check,board)
            board[check[0],check[1]] = board[coords[0],coords[1]]
            board[coords[0],coords[1]] = 0
        else:
            push(dir,other,board,True)
            push(dir,check,board)
            board[check[0],check[1]] = board[coords[0],coords[1]]
            board[coords[0],coords[1]] = 0
    
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

    if can_push(dir,[coords[0]+dir[0],coords[1]+dir[1]],board):
        push(dir,[coords[0]+dir[0],coords[1]+dir[1]],board)
        return [coords[0]+dir[0],coords[1]+dir[1]]
    else:
        return coords
    
def score(board,max_id):
    tot = 0
    for id in range(1,max_id):
        box = list(zip(*[x for x in np.where(board == id)]))[0]
        tot += 100*box[0]+box[1]
    
    return tot

board,pos,max_id = parse(board_r)
moves = [x for x in moves_r if x != '\n']
#print(board)
steps = len(moves)
for i in range(steps):
    pos = move(pos,moves[i])
    #print(i,pos)
    #print(board)

#print(board)
print(score(board,max_id))