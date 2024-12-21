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
    def __init__(self,pos,face,steps=0,turns=0,hist=set()):
        self.pos = pos
        self.face = face
        self.steps = steps
        self.turns = turns
        self.hist = hist

    def advance(self):
        self.pos[0] += self.face[0]
        self.pos[1] += self.face[1]
        
    def move(self,board):
        ret = []
        if board[self.pos[0]+rot90(self.face)[0],self.pos[1]+rot90(self.face)[1]] == '.':
            newInst = dfsInstance([self.pos[0],self.pos[1]],rot90(self.face),self.steps+1,self.turns+1,self.hist.copy())
            newInst.advance()
            ret.append(newInst)
            
        if board[self.pos[0]+rot270(self.face)[0],self.pos[1]+rot270(self.face)[1]] == '.':
            newInst = dfsInstance([self.pos[0],self.pos[1]],rot270(self.face),self.steps+1,self.turns+1,self.hist.copy())
            newInst.advance()
            ret.append(newInst)
        
        if board[self.pos[0]+self.face[0],self.pos[1]+self.face[1]] == '.':
            self.advance()
            self.steps += 1
            ret.append(self)
            
        return ret

    def add_hist(self,pos):
        if pos not in self.hist:
            self.hist.add(pos)

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
    best_paths = []
    toCheck = [dfsInstance(start,[0,1])]
    score_arr = np.array([[-1 for _ in range(board.shape[1])] for _ in range(board.shape[0])])
    rec = 0
    while len(toCheck) > 0:
        if len(toCheck) > rec:
            rec = len(toCheck)
            #print(rec)
        #print([[[int(x) for x in x.pos],x.turns,x.steps] for x in toCheck])
        next_inst = toCheck.pop()
        next_inst.add_hist(get_str_coords(next_inst.pos.copy()))
        prev_arr = score_arr[next_inst.pos[0],next_inst.pos[1]]
        score_pos = score_arr[next_inst.pos[0],next_inst.pos[1]]
        #print('hi',len(np.where(score_arr != -1)[0]))
        if score_pos != -1 and score_pos < (next_inst.turns-1)*1000+next_inst.steps:
            continue
        adv_inst = next_inst.move(board)
        for inst in adv_inst:
            #print(score_arr[inst.pos[0],inst.pos[1]],inst.turns*1000+inst.steps)
            if score_arr[inst.pos[0],inst.pos[1]] == -1 or score_arr[inst.pos[0],inst.pos[1]] > inst.turns*1000+inst.steps:
                score_arr[inst.pos[0],inst.pos[1]] = inst.turns * 1000 + inst.steps
            if inst.pos == end and ((found and (inst.turns*1000+inst.steps) <= best) or not found):
                found = True
                new_best = inst.turns*1000+inst.steps
                #print('hi',new_best)
                if new_best != best:
                    best_paths = [inst.hist]
                else:
                    best_paths.append(inst.hist)
                best = new_best
            elif found and (inst.turns*1000+inst.steps) > best:
                continue
            else:
                toCheck.append(inst)
    return best, best_paths

def print_path(board,path):
    board = board.copy()
    for pos in path:
        board[pos[0],pos[1]] = 'O'
    print('\n'.join([''.join(board[:,r]) for r in range(board.shape[0])]))

def print_board(board):
    text = '\n'.join([' '.join(str(x)) for x in board])
    with open('temp_out.txt','w') as f:
        f.write(text)
    
def get_str_coords(coords):
    return ' '.join([str(x) for x in coords])
    
board,start,end = parse(real_board)
board[start[0],start[1]] = '.'
board[end[0],end[1]] = '.'
dfs_result,best_paths = dfs(board,start,end)
print(dfs_result)
pts_set = set()
for path in best_paths:
    for pos in path:
        pts_set.add(pos)

print(len(pts_set)+1)