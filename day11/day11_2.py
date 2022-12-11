# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:47:32 2022

@author: UzsekaDaniel
"""

itemList = { 0 : [98, 70, 75, 80, 84, 89, 55, 98],
             1 : [59],
             2 : [77, 95, 54, 65, 89],
             3 : [71, 64, 75],
             4 : [74, 55, 87, 98],
             5 : [90, 98, 85, 52, 91, 60],
             6 : [99, 51],
             7 : [98, 94, 59, 76, 51, 65, 75]}

activityCnt = [0, 0, 0, 0, 0, 0, 0, 0]

mod = 11 * 19 * 7 * 17 * 3 * 5 * 13 * 2

for i in range(10000):
    for j in range(8):
        #itemList[j].sort()
        for item in itemList[j]:
            if(0 == j):     item *= 2
            elif(1 == j):   item *= item
            elif(2 == j):   item += 6
            elif(3 == j):   item += 2
            elif(4 == j):   item *= 11
            elif(5 == j):   item += 7
            elif(6 == j):   item += 1
            elif(7 == j):   item += 5
            
            #item = int(item / 3)
            if item >= mod:
                item %= mod
            
            if(0 == j):     target = (4, 1)[0 == (item % 11)]
            elif(1 == j):   target = (3, 7)[0 == (item % 19)]
            elif(2 == j):   target = (5, 0)[0 == (item % 7)]
            elif(3 == j):   target = (2, 6)[0 == (item % 17)]
            elif(4 == j):   target = (7, 1)[0 == (item % 3)]
            elif(5 == j):   target = (4, 0)[0 == (item % 5)]
            elif(6 == j):   target = (2, 5)[0 == (item % 13)]
            elif(7 == j):   target = (6, 3)[0 == (item % 2)]
            
            itemList[target].append(item)

            activityCnt[j] += 1
        itemList[j].clear()
activityCnt.sort(reverse=True)
print(activityCnt[0] * activityCnt[1])