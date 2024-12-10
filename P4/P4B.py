import numpy as np

with open('Input4.txt', 'r') as file:
    real = file.read()
      
example2 = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

test = np.array([
  ['M','#','S'],
  ['#','A','#'],
  ['M','#','S']
  ])
  
def parse(in_str):
  return np.array([list(s) for s in in_str.split('\n')])

def check_if_same(arr1,check):
  for row in range(3):
    for col in range(3):
      if not (arr1[row,col] == check[row,col] or check[row,col] == '#'):
        return False
  return True
    
  
def check_all_rot(arr1,check):
  for i in range(4):
    if check_if_same(arr1,check):
      return True
    check = np.rot90(check)
  return False

def check_pos_slices(board):
  ct = 0
  for r in range(np.shape(board)[0]-2):
    for c in range(np.shape(board)[1]-2):
      if check_all_rot(board[r:r+3,c:c+3],test):
        ct += 1
  return ct
  
str_example = parse(real)
print(check_pos_slices(str_example))


