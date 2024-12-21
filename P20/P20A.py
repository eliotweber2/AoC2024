import numpy as np 

with open('Input20.txt') as f:
  real = f.read()

example_input = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''

def create_score_map(board):
  board = np.array([list(x) for x in board.split('\n')])
  score_map = np.zeros(board.shape)
  curr_ind = list(list(zip(*np.where(board == 'S')))[0])
  start = curr_ind.copy()
  end = list(list(zip(*np.where(board == 'E')))[0])
  board[end[0],end[1]] = '.'
  hist = []
  curr_steps = 0
  while not np.array_equal(curr_ind,end):
    score_map[curr_ind[0],curr_ind[1]] = curr_steps
    hist.append(curr_ind.copy())
    curr_steps += 1
    #print(curr_ind)
    curr_ind = get_fwd(board,hist,curr_ind,find_neighbors)[0]
  
  score_map[end[0],end[1]] = curr_steps
  return start,end,board,score_map

def get_fwd(board,hist,pos,fn):
  return [x for x in fn(board,pos) if x not in hist]
  
def find_neighbors(board,pos):
  neighbor_inds = []
  if board[pos[0]-1,pos[1]] == '.':
    neighbor_inds.append([pos[0]-1,pos[1]])
  if board[pos[0]+1,pos[1]] == '.':
    neighbor_inds.append([pos[0]+1,pos[1]])
  if board[pos[0],pos[1]-1] == '.':
    neighbor_inds.append([pos[0],pos[1]-1])
  if board[pos[0],pos[1]+1] == '.':
    neighbor_inds.append([pos[0],pos[1]+1])
  return neighbor_inds
  
def find_walls(board,pos):
  neighbor_inds = []
  if pos[0] > 0 and board[pos[0]-1,pos[1]] == '#':
    neighbor_inds.append([pos[0]-1,pos[1]])
  if pos[0] < board.shape[0]-2 and board[pos[0]+1,pos[1]] == '#':
    neighbor_inds.append([pos[0]+1,pos[1]])
  if pos[0] > 0 and board[pos[0],pos[1]-1] == '#':
    neighbor_inds.append([pos[0],pos[1]-1])
  if pos[1] < board.shape[1]-2 and board[pos[0],pos[1]+1] == '#':
    neighbor_inds.append([pos[0],pos[1]+1])
  return neighbor_inds

def check_all_walls(curr_ind,end,board,score_map,hack_min):
  valid_hacks = 0
  hist = []
  while curr_ind != end:
    for wall in get_fwd(board,[],curr_ind,find_walls):
      for poss in get_fwd(board,[],wall,find_neighbors):
        #print(wall,poss,score_map[poss[0],poss[1]],score_map[curr_ind[0],curr_ind[1]]);
        if score_map[poss[0],poss[1]] - score_map[curr_ind[0],curr_ind[1]] > hack_min:
          valid_hacks += 1
    curr_ind = get_fwd(board,hist,curr_ind,find_neighbors)[0]
    hist.append(curr_ind.copy())
  
  return valid_hacks

start,end,board,score_map = create_score_map(real)

print(score_map)
print(check_all_walls(start,end,board,score_map,100))


