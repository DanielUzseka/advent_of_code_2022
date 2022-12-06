# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 10:17:38 2022

@author: UzsekaDaniel
"""

f = open("day6_data.txt", "r")
Lines = f.readlines()

count = 0
line = list(Lines[0])
data = []


# Strips the newline character
for c in line:
    count += 1
    if(count > 14):
        data.append(c)
        data.pop(0)
        if len(set(data)) == len(data):
            break
    else:
        data.append(c)

f.close()

print(count)