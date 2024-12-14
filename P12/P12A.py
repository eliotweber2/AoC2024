import numpy as np
from copy import deepcopy

with open('input12.txt') as f:
  real_str = f.read()

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
  return nodeLst
  
def calcPerimeter(board):
  perimeterArr = np.zeros(board.shape)
  for r in range(board.shape[0]):
    for c in range(board.shape[1]):
      neighbors = [board[node[0],node[1]]  for node in getVNeighbors(r,c,board.shape) + getHNeighbors(r,c,board.shape)]
      perimeterArr[r,c] = 4 - neighbors.count(board[r,c])
  return perimeterArr
  
def calcPrice(regions,perimeterArr):
  tot = 0
  for region in regions:
    region_perimeter = 0
    for node in region:
      region_perimeter += perimeterArr[node[0],node[1]]
    tot += region_perimeter * len(region)
    #print(len(region),region_perimeter,region_perimeter*len(region))
  return tot
  
real = parse(real_str)
example2 = parse(example2_str)
area = classify(real)
perimeterArr = calcPerimeter(real)
print(calcPrice(area,perimeterArr))