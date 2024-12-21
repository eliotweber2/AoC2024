import numpy as np 

with open('Input16.txt') as f:
    real_board = f.read()

example_board = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''

class dfsInstance:
    def __init__(self,pos,face,steps=0,turns=0):
        self.pos = pos
        self.face = face
        self.steps = steps
        self.turns = turns

    def advance(self):
        self.pos[0] += self.face[0]
        self.pos[1] += self.face[1]
        
    def move(self,board):
        ret = []
        if board[self.pos[0]+rot90(self.face)[0],self.pos[1]+rot90(self.face)[1]] == '.':
            newInst = dfsInstance([self.pos[0],self.pos[1]],rot90(self.face),self.steps+1,self.turns+1)
            newInst.advance()
            ret.append(newInst)
            
        if board[self.pos[0]+rot270(self.face)[0],self.pos[1]+rot270(self.face)[1]] == '.':
            newInst = dfsInstance([self.pos[0],self.pos[1]],rot270(self.face),self.steps+1,self.turns+1)
            newInst.advance()
            ret.append(newInst)
        
        if board[self.pos[0]+self.face[0],self.pos[1]+self.face[1]] == '.':
            self.advance()
            self.steps += 1
            ret.append(self)
            
        return ret

def parse(str_board):
    board = np.array([list(x) for x in str_board.split('\n')])
    start = list(list(zip(*np.where(board == 'S')))[0])
    end = list(list(zip(*np.where(board == 'E')))[0])
    return board,start,end
    
def rot90(face):
    if face == [-1,0]:
        return [0,1]
    if face == [1,0]:
        return [0,-1]
    if face == [0,-1]:
        return [-1,0]
    if face == [0,1]:
        return [1,0]
    
def rot270(face):
    if face == [-1,0]:
        return [0,-1]
    if face == [1,0]:
        return [0,1]
    if face == [0,-1]:
        return [1,0]
    if face == [0,1]:
        return [-1,0]
    
def dfs(board,start,end):
    found = False
    best = 0
    toCheck = [dfsInstance(start,[0,1])]
    score_arr = np.array([[-1 for _ in range(board.shape[1])] for _ in range(board.shape[0])])
    while len(toCheck) > 0:
        #print([[[int(x) for x in x.pos],x.turns,x.steps] for x in toCheck])
        next_inst = toCheck.pop()
        score_pos = score_arr[next_inst.pos[0],next_inst.pos[1]]
        if score_pos == -1 or score_pos > next_inst.turns * 1000 + next_inst.steps:
            score_arr[next_inst.pos[0],next_inst.pos[1]] = next_inst.turns * 1000 + next_inst.steps
        else:
            continue
        adv_inst = next_inst.move(board)
        for inst in adv_inst:
            if inst.pos == end and ((found and (inst.turns*1000+inst.steps) < best) or not found):
                found = True
                best = inst.turns*1000+inst.steps
            elif found and (inst.turns*1000+inst.steps) > best:
                #print('deleted')
                continue
            else:
                toCheck.append(inst)
    return best

def print_score_arr(arr):
    ret_str = ''
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            if arr[r,c] == -1:
                    ret_str += '.'
            else:
                    ret_str += '#'
        ret_str += '\n'
    return ret_str
    
    print(dead_ends) 
    print(score_arr)
    return best
    
def get_str_coords(coords):
    return ' '.join([str(x) for x in coords])
    
board,start,end = parse(real_board)
board[start[0],start[1]] = '.'
board[end[0],end[1]] = '.'
dfs_result = dfs(board,start,end)
print(dfs_result)


