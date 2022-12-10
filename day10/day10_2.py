# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:58:58 2022

@author: UzsekaDaniel
"""

with open('day10_data.txt', 'r') as f:
    Lines = f.readlines()
    
progCnt = 0
program = Lines[progCnt].strip().split(" ")
x = 1
sumStren = 0
state = 1
render = ""

for i in range(1,240):
    
    if(abs((i%40-1) - x) <= 1):
        render += "#"
    else:
        render += "."
        
    if(i%40 == 0):
        render += "\n"
    
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
    
print(render)