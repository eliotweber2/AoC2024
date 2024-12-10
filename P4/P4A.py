import numpy as np

with open('Input4.txt', 'r') as file:
    real = file.read()
    
example = np.array([
  ['.','.','X','.','.','.'],
  ['.','S','A','M','X','.'],
  ['.','A','.','.','A','.'],
  ['X','M','A','S','.','S'],
  ['.','X','.','.','.','.']])
  
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
  
rows,cols = np.shape(example)

fwd = ['X','M','A','S']
back = ['S','A','M','X']

def parse(in_str):
  return np.array([list(s) for s in in_str.split('\n')])

def ct_in_arr(sub,arr):
  ct = 0
  for i in range(len(arr)-len(sub)+1):
    if np.array_equal(arr[i:i+len(sub)],sub):
      ct += 1
      
  return ct
  
def check_rows(board,cols):
  return sum([ct_in_arr(fwd,board[i,:]) + ct_in_arr(back,board[i,:]) for i in range(cols)])
  
def check_cols(board,rows):
  return sum([ct_in_arr(fwd,board[:,i]) + ct_in_arr(back,board[:,i]) for i in range(rows)])
  
def check_diag(board,rows):
  return sum([ct_in_arr(fwd,np.diag(board,i)) + ct_in_arr(back,np.diag(board,i)) for i in range(-1*rows,rows)])
  
def check_invs(board,rows):
  return sum([ct_in_arr(fwd,np.diag(np.fliplr(board),i)) + ct_in_arr(back,np.diag(np.fliplr(board),i)) for i in range(-1*rows,rows)])
  
def check_all(board):
  num_rows,num_cols = np.shape(board)
  rows = check_rows(board,num_rows)
  cols = check_cols(board,num_cols)
  diag = check_diag(board,num_rows)
  invs = check_invs(board,num_rows)
  return rows + cols + diag + invs
  
  
str_example = parse(real)
print(check_all(str_example));


