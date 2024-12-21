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
  for i in range(board.shape[0]):
    for j in range(board.shape[1]):
      if board[i,j] == '#':
        score_map[i,j] = -1
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
  return board,score_map

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

def check_all(board,score_map,min_hack):
    edges = set()
    for i in range(int(score_map.max())):
        loc = list(zip(*np.where(score_map == i)))[0]
        for dx in range(-20,21):
          for dy in range(-20,21):
            if abs(dx) + abs(dy) <= 20:
              if loc[0]+dx >= 0 and loc[0]+dx < board.shape[0] and loc[1]+dy >= 0 and loc[1]+dy < board.shape[1]:
                if score_map[loc[0]+dx,loc[1]+dy] - score_map[loc[0],loc[1]] - abs(dx) - abs(dy) >= min_hack:
                  edges.add((loc[0],loc[1],loc[0]+dx,loc[1]+dy))
    return len(edges)

    

board,score_map = create_score_map(real)
print('hi')
print(check_all(board,score_map,100))

#print(score_map)

