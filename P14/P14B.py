import sys
import re
import numpy as np
import math

#np.set_printoptions(threshold=sys.maxsize)

#size = [11,7]
size = [101,103]

with open('./Input14.txt') as f:
    real = f.read()

example = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''

class Drone:
    def __init__(self,pos,vel,size):
        self.pos = pos
        self.vel = vel
        self.size = size
    
    def move(self):
        self.pos[0] = (self.pos[0] + self.vel[0] + self.size[0]) % self.size[0]
        self.pos[1] = (self.pos[1] + self.vel[1] + self.size[1]) % self.size[1]

def parse(str):
    drones = []
    for line in str.split('\n'):
        nums = re.findall(r'-?\d+', line)
        pos = [int(nums[0]), int(nums[1])]
        vel = [int(nums[2]), int(nums[3])]
        drones.append(Drone(pos, vel, size))
    return drones

def get_arr(drones):
    board = np.zeros([size[1],size[0]])
    for drone in drones:
        board[drone.pos[1], drone.pos[0]] += 1
    return board

def score(drones):
    qs = [0,0,0,0]
    midH = (size[0] - 1) / 2
    midV = (size[1] - 1) / 2
    for drone in drones:
        if drone.pos[0] < midH and drone.pos[1] < midV:
            qs[0] += 1
        elif drone.pos[0] > midH and drone.pos[1] < midV:
            qs[1] += 1
        elif drone.pos[0] < midH and drone.pos[1] > midV:
            qs[2] += 1
        elif drone.pos[0] > midH and drone.pos[1] > midV:
            qs[3] += 1
    print(qs)
    return qs[0] * qs[1] * qs[2] * qs[3]

def to_str(drones):
    board = get_arr(drones)
    str_p = ''
    for row in board:
        for cell in row:
            if cell == 0:
                str_p += '.'
            else:
                str_p += str(int(cell))
        str_p += '\n'
    return str_p

drones = parse(real)
#print_board(drones)
steps = 0
while steps < 7750:
    for drone in drones:
        drone.move()
    steps += 1

while True:
    for drone in drones:
        drone.move()
    #print(to_str(drones))
    with open('./P14BViewer.txt', 'w') as f:
        f.write(to_str(drones) + '\n'+ str(steps))
    print(steps)
    input()
    steps += 1

#tree at 7752
#ans = 7753