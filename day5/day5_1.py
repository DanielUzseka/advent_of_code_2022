# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 10:17:11 2022

@author: UzsekaDaniel
"""

f = open("day5_data.txt", "r")
Lines = f.readlines()
status = 0
data = {}  


# Strips the newline character
for line in Lines:
    newLine = line.strip()
    if len(newLine) == 0:
        status = 1
    elif status == 0:
        cnt = 0
        for c in line:
            cnt += 1
            if c.isalpha():
                col = (cnt - 2) / 4 + 1
                if col in data.keys():
                    data[col].append(c)
                else:
                    data[col] = [c]
    elif status == 1:
        commands = newLine.split(" ")
        quantity = int(commands[1])
        source = int(commands[3])
        destination = int(commands[5])
        
        for i in range(quantity):
            data[destination].insert(0, data[source].pop(0))
        print(data)

f.close()

for key in sorted(data):
    print ("%s: %s" % (key, data[key].pop(0)))
