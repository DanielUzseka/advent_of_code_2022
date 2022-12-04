# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:01:49 2022

@author: UzsekaDaniel
"""

f = open("day3_data.txt", "r")
Lines = f.readlines()
  
sumPrio = 0

# Strips the newline character
for line in Lines:
    newLine = line.strip()
    
    first = line[0:int(len(newLine)/2)]
    second = line[int(len(newLine)/2):int(len(newLine))]
    
    for c in first:
        if c in second: 
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                sumPrio += ord(c) - ord('a') + 1
            elif c >= 'A' and c <= 'Z':
                sumPrio += ord(c) - ord('A') + 27
            break

f.close()

print(sumPrio)