import numpy as np

with open('Input12.txt') as f:
    real = f.read()

example = np.array([
    ['A','A','A','A'],
    ['B','B','C','D'],
    ['B','B','C','C'],
    ['E','E','E','C']
])

example2_str = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''

example3 = '''AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA'''
        
def parse(board):
    return np.array([list(row) for row in board.split('\n')])
        
def getHNeighbors(r,c,dim):
    return_lst = []
    if r-1 >= 0:
        return_lst.append([r-1,c])
    if r+1 < dim[0]:
        return_lst.append([r+1,c])
    return return_lst
    
def getVNeighbors(r,c,dim):
    return_lst = []
    if c-1 >= 0:
        return_lst.append([r,c-1])
    if c+1 < dim[1]:
        return_lst.append([r,c+1])
    return return_lst
        
def classify(board):
    regionBoard = np.zeros(board.shape,dtype=object)
    regionId = 0
    regionLst = []
    for r in range(regionBoard.shape[0]):
        for c in range(regionBoard.shape[1]):
            regionBoard[r,c] = regionId
            regionLst.append(regionId)
            regionId += 1

    for r in range(regionBoard.shape[0]):
        for c in range(regionBoard.shape[1]):
            poss_lst = getHNeighbors(r,c,board.shape) + getVNeighbors(r,c,board.shape)
            for poss in poss_lst:
                if regionBoard[r,c] != regionBoard[poss[0],poss[1]] and board[r,c] == board[poss[0],poss[1]]:
                    regionLst = [poss_id for poss_id in regionLst if poss_id != regionBoard[poss[0],poss[1]]]
                    replace_inds = list(zip(*np.where(regionBoard == regionBoard[poss[0],poss[1]])))
                    for ind in replace_inds:
                        regionBoard[ind[0],ind[1]] = regionBoard[r,c]

    nodeLst = []             
    for region in regionLst:
        raw_inds = np.where(regionBoard == region)
        nodeLst.append(list(zip(*raw_inds)))
    return nodeLst,regionBoard

def getSides(start_edge,regionId,regionBoard):
    curr_edge = start_edge
    curr_dir = 'right'
    start_dir = 'right'
    checked = []
    ct = 0
    while ct == 0 or curr_edge != start_edge or curr_dir != start_dir:
        checked.append(curr_edge)
        #print(curr_edge,curr_dir,ct,regionBoard[curr_edge[0],curr_edge[1]])
        if curr_dir == 'right':
            if regionBoard[curr_edge[0]+1,curr_edge[1]] != regionId:
                curr_dir = 'down'
                ct += 1
            elif regionBoard[curr_edge[0],curr_edge[1]+1] == regionId:
                curr_dir = 'up'
                ct += 1
                
        elif curr_dir == 'down':
            if regionBoard[curr_edge[0],curr_edge[1]-1] != regionId:
                curr_dir = 'left'
                ct += 1
            elif regionBoard[curr_edge[0]+1,curr_edge[1]] == regionId:
                curr_dir = 'right'
                ct += 1
                
        elif curr_dir == 'left':
            if regionBoard[curr_edge[0]-1,curr_edge[1]] != regionId:
                curr_dir = 'up'
                ct += 1
            elif regionBoard[curr_edge[0],curr_edge[1]-1] == regionId:
                curr_dir = 'down'
                ct += 1

        elif curr_dir == 'up':
            if regionBoard[curr_edge[0],curr_edge[1]+1] != regionId:
                curr_dir = 'right'
                ct += 1
            elif regionBoard[curr_edge[0]-1,curr_edge[1]] == regionId:
                curr_dir = 'left'
                ct += 1
        if ct != 0 and curr_edge == start_edge and curr_dir == start_dir:
            return ct,checked
        if curr_dir == 'right' and regionBoard[curr_edge[0],curr_edge[1]+1] != regionId:
            curr_edge = [curr_edge[0],curr_edge[1]+1]
        elif curr_dir == 'down' and regionBoard[curr_edge[0]+1,curr_edge[1]] != regionId:
            curr_edge = [curr_edge[0]+1,curr_edge[1]]
        elif curr_dir == 'left' and regionBoard[curr_edge[0],curr_edge[1]-1] != regionId:
            curr_edge = [curr_edge[0],curr_edge[1]-1]
        elif curr_dir == 'up' and regionBoard[curr_edge[0]-1,curr_edge[1]] != regionId:
            curr_edge = [curr_edge[0]-1,curr_edge[1]]

    return ct,checked

def getAllSides(regionId,regionBoard):
    ct = 0
    checked = []
    while True:
        next_start = get_next_start(regionId,regionBoard,checked)
        if next_start is None:
            return ct
        new_ct,new_checked = getSides(next_start,regionId,regionBoard)
        checked += new_checked
        ct += new_ct

def get_next_start(regionId,regionBoard,checked):
    for r in range(regionBoard.shape[0]-1):
        for c in range(regionBoard.shape[1]):
            if regionBoard[r+1,c] == regionId and [r,c] not in checked and regionBoard[r,c] != regionId:
                return [r,c]
    return None

def getPrice(regionLst,regionBoard):
    ct = 0
    for region in regionLst:
        id = regionBoard[region[0][0]+1,region[0][1]+1]
        ct += getAllSides(id,regionBoard) * len(region)
        #print(example3[region[0][0],region[0][1]],regionBoard[region[0][0]+1,region[0][1]+1],getAllSides(id,regionBoard) * len(region))
    return ct

real = parse(real)
example2 = parse(example2_str)
example3 = parse(example3)
regionLst,regionBoard = classify(real)
regionBoard = np.pad(regionBoard,[(1,1),(1,1)],mode='constant',constant_values=-1)
print(regionBoard)
print(getPrice(regionLst,regionBoard))