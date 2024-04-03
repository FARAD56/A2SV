from math import *

def solve():
    n = int(input())
    s = input()
    nums = []
    for i in range(1, int(sqrt(n)) + 1):
        if not n % i:
            nums += [i]
            if i**2 != n:
                nums += [n // i]
    nums = sorted(nums)
    
    for k in range(len(nums)):
        long = nums[k]
        subarray = s[:long]
        end_leng = s[n - long:]
        count = arrange = 0
        
        for i in range(0, n, long):

            for j in range(i, i + long):

                if s[j] != subarray[j % long]: count += 1
                if s[j] != end_leng[j % long]: arrange += 1

        if 2 > count or arrange < 2:
            return long
        
for _ in range(int(input())):
    print(solve())
