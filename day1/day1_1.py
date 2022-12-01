# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:29:04 2022

@author: UzsekaDaniel
"""


f = open("day1_data.txt", "r")
Lines = f.readlines()
  
count = 0
maxCount = 0
# Strips the newline character
for line in Lines:
    if line.strip():
        count += int(line)
        # print(count)
    else:
        if count > maxCount:
            maxCount = count
        count = 0
        
f.close()

print(maxCount)
        