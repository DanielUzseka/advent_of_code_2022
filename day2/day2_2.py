# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 07:38:05 2022

@author: UzsekaDaniel
"""

f = open("day2_data.txt", "r")
Lines = f.readlines()
  
score = 0

# Strips the newline character
for line in Lines:
    line.strip()
    opp = ord(line[0]) - ord('A') + 1
    outcome = ord(line[2]) - ord('X')
    
    played = opp + (outcome - 1)
    
    if(played < 1):
        played += 3
    elif(played > 3):
        played -= 3
    

    score += (outcome)*3 + played
    
        
    print(played)


f.close()

print(score)