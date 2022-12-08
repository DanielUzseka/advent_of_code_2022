# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:33:44 2022

@author: UzsekaDaniel
"""

import numpy as np

f = open("day8_data.txt", "r")
Lines = f.readlines()
trees = []

# Strips the newline character
for line in Lines:
    newLine = line.strip()
    row =  [ int(c) for c in newLine]
    trees.append(row)

f.close()

treeArray = np.array(trees)
scores = np.zeros((len(treeArray),len(treeArray[0])))

count = 0

for i in range(1,len(treeArray)-1):
    for j in range(1,len(treeArray[0])-1):
        score = 1
        dist = abs(j-0)
        for k in reversed(range(0,j)):
            if(treeArray[i,k] >= treeArray[i,j]):
                dist = abs(j-k)
                break
        score *= dist

        dist = abs(j-len(treeArray)+1)
        for k in range(j+1,len(treeArray)):
            if(treeArray[i,k] >= treeArray[i,j]):
                dist = abs(j-k)
                break
        score *= dist
        
        dist = abs(i-0)
        for k in reversed(range(0,i)):
            if(treeArray[k,j] >= treeArray[i,j]):
                dist = abs(i-k)
                break
        score *= dist
        
        dist = abs(i-len(treeArray)+1)
        for k in range(i+1,len(treeArray)):
            if(treeArray[k,j] >= treeArray[i,j]):
                dist = abs(i-k)
                break
        score *= dist
        
        scores[i,j] = score

print(np.amax(scores))