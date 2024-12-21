import numpy as np 
import re

with open('Input18.txt') as f:
    real = f.read()

example_board = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''

def create_board(locs):
  board = np.zeros([71,71])
  allowed = locs.split('\n')[:2912]
  print(allowed[-1])
  for loc in allowed:
    coords = [int(x) for x in re.findall(r'\d+',loc)]
    #print(coords)
    board[coords[1],coords[0]] = 1 
  
  return board

class BFSInstance():
  def __init__(self,pos,visited=[],steps=0):
    self.pos = pos
    self.visited = visited
    self.steps = steps
  
  def getNext(self,board):
    nextNodes = []
    poss = getNeighbors(self.pos,board)
    for coords in poss:
      if board[coords[0],coords[1]] == 0 and coords not in self.visited:
        newNode = BFSInstance(coords,self.visited,self.steps+1)
        newNode.visited.append(coords.copy())
        nextNodes.append(newNode)
        
    return nextNodes
    
def getNeighbors(pos,board):
  neighbors = []
  for x in range(-1,2):
    for y in range(-1,2):
      if (x != 0 or y != 0) and (x == 0 or y == 0):
        if (pos[0]+x >= 0 and pos[0]+x < board.shape[0]) and (pos[1]+y >= 0 and pos[1]+y < board.shape[1]):
          neighbors.append([pos[0]+x,pos[1]+y])
          
  return neighbors
  
def bfs(board,start,end):
  queue = [BFSInstance(start,[start])]
  while len(queue) != 0:
    nextNode = queue.pop(0)
    #print(nextNode.pos,len(queue))
    for node in nextNode.getNext(board):
      if np.array_equal(node.pos,end):
        print('hi',node.visited)
        return node.steps
      queue.append(node)
      
example = create_board(real)
#print(example)
#print(bfs(example,[0,0],[70,70]))
      
