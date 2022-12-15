# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 09:55:42 2022

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

for i in range(xmin - max(distances), xmax+1 + max(distances)):
#for i in range(10):
    print(i)
    for j in range(len(sensors)):
        actDist = (abs(i - sensors[j][0]) + abs(y - sensors[j][1]))
        if  (actDist <= distances[j]):
            if((i, y) != beacons[j]):
                cnt += 1
            break

print(cnt)

    
