# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:40:56 2022

@author: UzsekaDaniel
"""

f = open("day1_data.txt", "r")
Lines = f.readlines()
  
count = 0
maxCount = [0]
# Strips the newline character
for line in Lines:
    if line.strip():
        count += int(line)
        # print(count)
    else:
        if min(maxCount) < count:
            maxCount.remove(min(maxCount))
        if len(maxCount) < 3:
            maxCount.append(count)
            
        count = 0

f.close()

print(sum(maxCount))