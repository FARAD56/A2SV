#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    value, index = arr[n-1], n-1
    
    while index > 0 and value < arr[index-1]:
        arr[index] = arr[index-1]
        print(*arr)
        index -= 1
        
    arr[index] = value
    print(*arr)

    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
