# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:35:41 2022

@author: UzsekaDaniel
"""

maps = []
starts = {}
end = ()
rowCnt = 0
steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]


with open('day12_data.txt', 'r') as f:
    Lines = f.readlines()
    
for line in Lines:
    newLine = line.strip()
    row =  [ord(c) - ord("a") for c in newLine]
    for i in range(len(row)):
        if (row[i] == ord("S") - ord('a') or row[i] == 0):
            row[i] = 0
            start = (rowCnt, i)
            starts[start] = 0
        elif(row[i] == ord("E") - ord("a")):
            row[i] = ord("z") - ord("a")
            end = (rowCnt, i)
    maps.append(row)
    rowCnt += 1
    
for start in starts:
    visited = [ [0]*len(maps[0]) for i in range(len(maps)) ]
    pos = start
    visited[pos[0]][pos[1]] = 1
    found = False
    frontier = {}
    length = 0

    while(found == False):
        for i in steps:
            newPos = (pos[0] + i[0], pos[1] + i[1])
            #print(newPos)
            if(newPos[0] >= 0 and newPos[1] >= 0 and newPos[0] < len(maps) and newPos[1] < len(maps[0])):
                if(visited[newPos[0]][newPos[1]] == 0 and maps[newPos[0]][newPos[1]] - maps[pos[0]][pos[1]] <= 1):
                    frontier[newPos] = length + 1
        
        if(len(frontier) == 0):
            starts[start] = 999
            break
        pos = min(frontier, key=frontier.get)
        length = frontier[pos]
        frontier.__delitem__(pos)
        visited[pos[0]][pos[1]] = 1
        if(pos == end):
            found = True
            starts[start] = length
            
print(starts[min(starts, key=starts.get)])
    