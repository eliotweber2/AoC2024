import numpy as np

with open('./Input10.txt','r') as f:
    string = f.read()

example = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

def search(r,c,arr):
  cont = False
  ct = 0
  if arr[r,c] == '9':
    #print(r,c)
    return 1
  neighbors = get_neighbors(r,c,arr)
  for neighbor in neighbors:
    #print(neighbor,arr[neighbor[0],neighbor[1]],arr[r,c])
    if int(arr[r,c]) + 1 == int(arr[neighbor[0],neighbor[1]]):
      #print(r,c)
      if (result := search(neighbor[0],neighbor[1],arr)):
        ct += result
        cont = True
  if not cont:
    return False
  return ct
        
def search_v2(r,c,arr):
  visited = np.zeros(arr.shape,dtype=bool)
  to_check = [[r,c]]
  ct = 0
  while True:
    if len(to_check) == 0:
      return ct
    next_sq = to_check.pop()
    for poss in get_neighbors(next_sq[0],next_sq[1],arr):
      if int(arr[poss[0],poss[1]]) == int(arr[next_sq[0],next_sq[1]]) + 1 and not visited[poss[0],poss[1]]:
        visited[poss[0],poss[1]] = True
        if arr[poss[0],poss[1]] == '9':
          ct += 1
        else:
          to_check.append([poss[0],poss[1]])

def get_starts(arr):
  inds = list(zip((ind := np.where(arr == '0'))[0],ind[1]))
  return [[int(x[0]),int(x[1])] for x in inds]

def get_neighbors(r,c,arr):
  neighbors = []
  if r-1 >= 0:
    neighbors.append([r-1,c])
  if r+1 < arr.shape[0]:
    neighbors.append([r+1,c])
  if c-1 >= 0:
    neighbors.append([r,c-1])
  if c+1 < arr.shape[1]:
    neighbors.append([r,c+1])
  return neighbors

arr = np.array([list(r) for r in string.split('\n')])
tot = 0;
#print(arr)
starts = get_starts(arr)
for start in starts:
  tot += result if (result := search(start[0],start[1],arr)) else 0
  #print(result)

print(tot)


