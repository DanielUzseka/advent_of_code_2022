# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:08:18 2022

@author: UzsekaDaniel
"""

f = open("day4_data.txt", "r")
Lines = f.readlines()
  
counter = 0

# Strips the newline character
for line in Lines:
    newLine = line.strip()
    test = newLine.split(",")
    first = [int(a) for a in test[0].split("-")]
    second = [int(a) for a in test[1].split("-")]
    
    if (first[0] >= second[0] and first[1] <= second[1]) or (first[0] <= second[0] and first[1] >= second[1]):
        counter += 1


f.close()

print(counter)