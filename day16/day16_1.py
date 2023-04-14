# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 08:59:17 2022

@author: UzsekaDaniel
"""

f = open("day16_data.txt", "r")
Lines = f.readlines()
path = {}
start = "AA"
rates = {}

# Strips the newline character
for line in Lines:
    line = line.strip()
    temp = line.split(" ")
    rates[temp[1]] = int(temp[4][5:-1])
    dests = []
    for i in range(9, len(temp)):
        dests.append(temp[i].strip(","))
    path[temp[1]] = dests

print(path)
print(rates)

visited = {}
current = [start]

for key in rates.keys():
    if rates[key] != 0:
        visited[key] = False
    else:
        visited[key] = True

for i in range(30):
    elem = current[-1]
    frontier = {}
    frontier = path[elem].copy()
    if(visited[elem] == False):
        frontier.append(elem)
    print(frontier)
    nextElem = frontier.pop()
    if(elem == nextElem):
        visited[elem] = True
    current.append(nextElem)
    print(current)

print(current)