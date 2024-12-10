import numpy as np
from math import sqrt
from itertools import combinations
import fractions

with open('Input8.txt') as f:
    real = f.read()

example = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''

arr = np.array([list(row) for row in real.split('\n')])

def find_line(p1,p2):
    slope = fractions.Fraction((p2[1]-p1[1]),(p2[0]-p1[0]))
    coff = slope.numerator
    roff = slope.denominator
    pts = []
    test_p = p1 if p1[1] < p2[1] else p2
    while True:
        if (test_p[0] < 0 or test_p[0] >= arr.shape[0] or test_p[1] < 0 or test_p[1] >= arr.shape[1]):
            break
        if int(test_p[1]) == test_p[1]:
            pts.append(test_p)
        test_p = (test_p[0]+roff, test_p[1]+coff)
    test_p = p1 if p1[1] > p2[1] else p2
    while True:
        if (test_p[0] < 0 or test_p[0] >= arr.shape[0] or test_p[1] < 0 or test_p[1] >= arr.shape[1]):
            break
        if int(test_p[1]) == test_p[1]:
            pts.append(test_p)
        test_p = (test_p[0]-roff, test_p[1]-coff)
    return pts

def check_pts(pts,p1,p2):
    correct = []
    for pt in pts:
        dst1 = sqrt((pt[0]-p1[0])**2 + (pt[1]-p1[1])**2)
        dst2 = sqrt((pt[0]-p2[0])**2 + (pt[1]-p2[1])**2)
        if dst1 == dst2 * 2 or dst2 == dst1 * 2:
            correct.append(pt)
    return correct
        

def find_antennas(arr):
    antennas = np.where(arr != '.')
    antennas = list(zip(antennas[0], antennas[1]))
    return classify(antennas, arr)

def classify(antennas, arr):
    antenna_dict = {}
    for antenna in antennas:
        if arr[antenna[0], antenna[1]] not in antenna_dict.keys():
            antenna_dict[arr[antenna[0], antenna[1]]] = [antenna]
        else:
            antenna_dict[arr[antenna[0], antenna[1]]].append(antenna)
    return antenna_dict

def check_pair(p1,p2):
    pts = find_line(p1,p2)
    #correct_pts = check_pts(pts,p1,p2)
    for point in pts:
        arr[point[0],int(point[1])] = 'X'
        if point not in correct:
            correct.append(point)

correct = []
antennas = find_antennas(arr)
#print(antennas)

to_check = [list(combinations(antennas[key], 2)) for key in antennas.keys()]
flat_to_check = [item for sublist in to_check for item in sublist]
for pair in flat_to_check:
    check_pair(pair[0],pair[1])

#check_pair([1,8],[2,5])
#print(arr)
print(len(correct))
