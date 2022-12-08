# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:28:09 2022

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

count = 0

for i in range(1,len(treeArray)-1):
    for j in range(1,len(treeArray[0])-1):
        if(max(treeArray[i,0:j]) >= treeArray[i,j] and max(treeArray[i,j+1:]) >= treeArray[i,j] and
           max(treeArray[0:i,j]) >= treeArray[i,j] and max(treeArray[i+1:,j]) >= treeArray[i,j] ):
            count += 1

print((len(treeArray)) * (len(treeArray[0])) - count)
