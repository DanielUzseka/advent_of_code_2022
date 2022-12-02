# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:24:08 2022

@author: UzsekaDaniel
"""

f = open("day2_data.txt", "r")
Lines = f.readlines()
  
score = 0

# Strips the newline character
for line in Lines:
    line.strip()
    opp = ord(line[0]) - ord('A') + 1
    played = ord(line[2]) - ord('X') + 1
    
    outcome = played - opp
    if(outcome < -1):
        outcome += 3
    elif (outcome > 1):
        outcome -= 3
    print(outcome)
    score += (outcome + 1)*3 + played
    
        
    print(played)


f.close()

print(score)