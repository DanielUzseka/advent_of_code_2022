# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:54:56 2022

@author: UzsekaDaniel
"""

with open('day9_data.txt', 'r') as f:
    Lines = f.readlines()
    
head = [0,0]
tail = [0,0]

moves = {(-2,-2):(-1,-1), (-2,-1):(-1,-1), (-2,0):(-1,0), (-2,1):(-1,1), 
         (-2,2):(-1,1), (-1,2):(-1,1), (0,2):(0,1), (1,2):(1,1), 
         (2,2):(1,1), (2,1):(1,1), (2,0):(1,0), (2,-1):(1,-1),
         (2,-2):(1,-1), (1,-2):(1,-1), (0,-2):(0,-1), (-1,-2):(-1,-1)}
visited = {(0,0):1}
    
for line in Lines:
    newLine = line.strip()
    x = 0
    y = 0
    data = newLine.split(" ")
    
    if(data[0] == "R"):
        x = 1
    elif (data[0] == "L"):
        x = -1
    elif (data[0] == "D"):
        y = -1
    elif (data[0] == "U"):
        y = 1
    
    for i in range(int(data[1])):
        head[0] += x
        head[1] += y
        diff = (head[0] - tail[0], head[1] - tail[1]) 
        if diff in moves.keys():
            tail[0] += moves[diff][0]
            tail[1] += moves[diff][1]

        if tuple(tail) not in visited.keys():
            visited[tuple(tail)] = 1

print(len(visited))
       