# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:33:07 2022

@author: UzsekaDaniel
"""

f = open("day7_data.txt", "r")
Lines = f.readlines()
tree = {"." : ["", 0]}
currDir = ""


# Strips the newline character
for line in Lines:
    newLine = line.strip()
    data = newLine.split(" ")
    if("$" == newLine[0]):
        #command
        command = data[1]
        if("cd" == command):
            if(".." == data[2]):
                currDir = tree[currDir][0]
            elif(data[2] == "/"):
                 currDir = "."
            else:
                currDir = currDir + "/" + data[2]
        elif("ls" == command):
            #do nothing
            print(currDir)
            continue
        
    else:
        if(not data[0].isalpha()):
            #file size
            tree[currDir][1] += int(data[0])
            parentDir = tree[currDir][0]
            while (parentDir != ""):
                tree[parentDir][1] += int(data[0])
                parentDir = tree[parentDir][0]
        elif("dir" == data[0]):
            if(data[1] not in tree.keys()):
                tree[currDir + "/" + data[1]] = [currDir, 0]
                #print(tree[data[1]])

f.close()

sum = 0

for key in tree.keys():
    if(tree[key][1] <= 100000):
        sum += tree[key][1]
        
print(sum)
    

