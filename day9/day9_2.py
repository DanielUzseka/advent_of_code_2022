# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 09:40:38 2022

@author: UzsekaDaniel
"""

with open('day9_data.txt', 'r') as f:
    Lines = f.readlines()
    
head = [0,0]
tail = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]

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
        print(len(tail))
        for j in range(len(tail)):
            if(0 == j):
                diff = (head[0] - tail[j][0], head[1] - tail[j][1]) 
            else:
                diff =(tail[j-1][0] - tail[j][0], tail[j-1][1] - tail[j][1])
            if diff in moves.keys():
                tail[j][0] += moves[diff][0]
                tail[j][1] += moves[diff][1]

            if tuple(tail[8]) not in visited.keys():
                visited[tuple(tail[8])] = 1

print(len(visited))