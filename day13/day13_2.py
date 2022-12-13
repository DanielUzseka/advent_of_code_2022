# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:13:19 2022

@author: UzsekaDaniel
"""

from functools import cmp_to_key

def compareLists(left, right):
    testVar = 0
    for i in range(min([len(left), len(right)])):
        if(type(left[i]) == type(testVar) and type(right[i]) == type(testVar)):
            if(left[i] > right[i]):
                return 1
            elif(left[i] < right[i]):
                return -1
        elif(type(left[i]) == type(testVar)):
            res = compareLists([left[i]], right[i]) 
            if (res != 0):
                return res
        elif(type(right[i]) == type(testVar)):
            res = compareLists(left[i], [right[i]]) 
            if (res != 0):
                return res
        else:
            res = compareLists(left[i], right[i]) 
            if (res != 0):
                return res
    if(len(left) > len(right)):
        return 1
    elif(len(left) < len(right)):
        return -1
    else:
        return 0
            
        
    

f = open("day13_data.txt", "r")
Lines = f.readlines()
idx = 0
dataCnt = 1
sums = 0
data = []

# Strips the newline character
for line in Lines:
    newLine = line.strip()
    if(len(newLine) != 0):
        data.append(eval(newLine))

data.append([[2]])
data.append([[6]])

compare_key = cmp_to_key(compareLists)
data.sort(key=compare_key)        

print((data.index([[2]]) + 1)* (data.index([[6]]) + 1))
    