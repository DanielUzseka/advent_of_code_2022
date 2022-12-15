# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 13:28:16 2022

@author: UzsekaDaniel
"""

f = open("day15_data.txt", "r")
Lines = f.readlines()
xmax = 0
xmin = 999999
ymax = 0
ymin = 999999
data = []
sensors = []
beacons = []
distances = []


# Strips the newline character
for line in Lines:
    line = line.strip()
    temp = line.split(":")
    sensor = (int(temp[0][temp[0].find("x=")+2:temp[0].rfind(",")]), int(temp[0][temp[0].find("y=")+2:]))
    beacon = (int(temp[1][temp[1].find("x=")+2:temp[1].rfind(",")]), int(temp[1][temp[1].find("y=")+2:]))
    sensors.append(sensor)
    beacons.append(beacon)
    distances.append(abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]))
    if xmax < sensor[0]: xmax = sensor[0]
    if xmax < beacon[0]: xmax = beacon[0]
    if ymax < sensor[1]: ymax = sensor[1]
    if ymax < beacon[1]: ymax = beacon[1]
    if xmin > sensor[0]: xmin = sensor[0]
    if xmin > beacon[0]: xmin = beacon[0]
    if ymin > sensor[1]: ymin = sensor[1]
    if ymin > beacon[1]: ymin = beacon[1]
    
y = 2000000
cnt = 0

for y in range(4000000):
    occ = []
    for j in range(len(sensors)):
        diff = abs(y - sensors[j][1])
        if(distances[j] > diff):
            actOcc = [sensors[j][0] - (distances[j] - diff), sensors[j][0] + distances[j] - diff]
            found = False
            for i in range(len(occ)):
                if occ[i][0] <= actOcc[1] and occ[i][0] > actOcc[0]: 
                    occ[i] = [actOcc[0], occ[i][1]]
                    found = True
                if occ[i][1] >= actOcc[0] and occ[i][1] < actOcc[1]:
                    occ[i] = [occ[i][0], actOcc[1]]
                    found = True
            if found == False:
                occ.append(actOcc)
    while(len(occ) > 1):
        temp = occ.pop()
        found = False
        for i in range(len(occ)):
            if occ[i][0] <= temp[1] and occ[i][0] > temp[0]: 
                occ[i] = [temp[0], occ[i][1]]
                found = True
                break
            elif occ[i][1] >= temp[0] and occ[i][1] < temp[1]:
                occ[i] = [occ[i][0], temp[1]]
                found = True
                break
            elif occ[i][0] <= temp[0] and occ[i][1] >= temp[1]:
                found = True
                break
        if(False == found):
            occ.append(temp)
            break
    
    if(len(occ) > 1):
        if(occ[0][0] > occ[1][1]):
            print((occ[0][0] - 1) * 4000000 + y)
        else:
            print((occ[1][0] - 1) * 4000000 + y)