# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:12:04 2022

@author: UzsekaDaniel
"""

f = open("day14_data.txt", "r")
Lines = f.readlines()
xmax = 0
xmin = 999
ymax = 0
data = []


# Strips the newline character
for line in Lines:
    line = line.strip()
    coords = line.split("->")
    first = True
    rocks = []
    for coord in coords:
        [x,y] = [int(i) for i in coord.split(",")]
        rocks.append((x,y))
        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y
        if x < xmin:
            xmin = x
    data.append(rocks)
    
xmax += 150
xmin -= 150
ymax += 2

cave = [ [0]*(xmax+1 - xmin) for i in range(ymax+1)]

for rocks in data:
    first = True
    last = ()
    for rock in rocks:
        if(True == first):
            cave[rock[1]][rock[0]-xmin] = 1
            first = False
        else:
            if(last[0] == rock[0]):
                step = 1
                if(last[1] < rock[1]):
                    step = -1
                for i in range(rock[1],last[1],step):
                    cave[i][rock[0]-xmin] = 1
            elif(last[1] == rock[1]):
                step = 1
                if(last[0] < rock[0]):
                    step = -1
                for i in range(rock[0],last[0],step):
                    cave[rock[1]][i-xmin] = 1
        last = rock
        
for i in range(xmin, xmax+1):
    cave[ymax][i-xmin] = 1
        
cave[0][500-xmin] = 3

start = (500, 0)
sand = start
keepGoing = True

while(keepGoing):
    landed = False
    sand = start
    while(False == landed):
        if((sand[0] - xmin - 1) >= 0 and (sand[0] + 1) <= xmax and (sand[1] + 1) <= ymax):
            if(cave[sand[1] + 1][sand[0] - xmin] == 0):
                sand = (sand[0], sand[1] + 1)
            elif(cave[sand[1] + 1][sand[0] - xmin - 1] == 0):
                sand = (sand[0] - 1, sand[1] + 1)
            elif(cave[sand[1] + 1][sand[0]- xmin + 1] == 0):
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                cave[sand[1]][sand[0] - xmin] = 2
                landed = True
                if(sand == start):
                    keepGoing = False
        else:
            landed = True
            keepGoing = False


cnt = 0
        
for i in cave:
    row = ""
    for j in i:
        if 1 == j:
            row += "#"
        elif 0 == j:
            row += "."
        elif 3 == j:
            row += "+"
        elif 2 == j:
            row += "o"
            cnt += 1
    print(row)
    
print(cnt)