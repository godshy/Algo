# reverse array
import os


def reverseArray(a):
    array_len = len(a)
    left = 0
    right = array_len - 1
    while left < right:
        temp = a[right]
        a[right] = a[left]
        a[left] = temp
        left+=1
        right-=1
    return a



arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))  # handile a series of inputs, make it int type using map, delete whitespace and insert into a list
res = reverseArray(arr)
print(res)