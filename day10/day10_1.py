# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:22:57 2022

@author: UzsekaDaniel
"""

with open('day10_data.txt', 'r') as f:
    Lines = f.readlines()
    
progCnt = 0
program = Lines[progCnt].strip().split(" ")
x = 1
sumStren = 0
state = 1

for i in range(1,220):
    if(program[0] == "noop"):
        progCnt += 1
        program = Lines[progCnt].strip().split(" ")
    elif(program[0] == "addx"):
        if(1 == state):
            state = 2
        elif(2 == state):
            state = 1
            x += int(program[1])
            progCnt += 1
            program = Lines[progCnt].strip().split(" ")

    if(19 == i or 59 == i or 99 == i or 139 == i or 179 == i):
        sumStren += x*(i+1)
        
sumStren += x*(220)
print(sumStren)
    