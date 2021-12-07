# An hourglass in is a subset of values with indices falling in this pattern in arr's graphical representation:
# Input size is limited as 6x6
import math
import os
import random
import re
import sys

def hourglassSum(arr):
    # print(arr)
    sumed = 0
    row = len(arr)
    temp = []
    temp_1 = []
    for row in range(4):
        for col in range(4):
            print(arr[row][col:col+3], arr[row+2][col:col+3], arr[row+1][col+1] )
            temp.append(sum(arr[row][col:col+3]) + sum(arr[row+2][col:col+3]) + arr[row+1][col+1])
        #print('temp: ', temp)
        temp_1.append(temp)
        #print('temp_1: ', temp_1)
        temp = []
    i = temp_1[0][0]
    print('temp_1: ', temp_1)
    for row in range(4):
        for col in range(4):
            if i <= temp_1[row][col]:
                i = temp_1[row][col]

    return i



arr = []

for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)
print(result)