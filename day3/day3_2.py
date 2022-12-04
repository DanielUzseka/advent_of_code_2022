# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 18:42:07 2022

@author: UzsekaDaniel
"""

f = open("day3_data.txt", "r")
Lines = f.readlines()
  
sumPrio = 0
dataType = 1

# Strips the newline character
for line in Lines:
    newLine = line.strip()
    
    if 1 == dataType:
        first = newLine
        dataType += 1
    elif 2 == dataType:
        second = newLine
        dataType += 1
    else:
        third = newLine
        dataType = 1
        for c in first:
            if c in second: 
                if c in third:
                    if ord(c) >= ord('a') and ord(c) <= ord('z'):
                        sumPrio += ord(c) - ord('a') + 1
                    elif c >= 'A' and c <= 'Z':
                        sumPrio += ord(c) - ord('A') + 27
                    break
    


f.close()

print(sumPrio)