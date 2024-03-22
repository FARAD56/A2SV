from itertools import accumulate
from bisect import *

for _ in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))

    def count_zeros(num):
        num = bin(num)[2:]
        return len(num) - len(num.rstrip('0'))

    number = 0
    even_idx = []

    for idx,num in enumerate(nums):
        number += count_zeros(num)
        if idx%2: even_idx.append(count_zeros(idx+1))

    even_idx.sort(reverse=True)
    even_idx = list(accumulate(even_idx))

    if number >= n:
        print(0)
    else:
        pos = bisect_left(even_idx, n-number)+1
        print(pos if pos <= len(even_idx) else -1)
