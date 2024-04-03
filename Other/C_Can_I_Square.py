from math import sqrt
t = int(input())

for _ in range(t):
    nums = sum(list(map(int, input().split())))

    l, r = 1, nums

    check = False
    while l <= r:
        mid = (r+l)//2

        if mid**2 > nums:
            r = mid -1
        elif mid**2 < nums:
            l = mid + 1
        else:
            print("YES")
            check = True
            break
    if not check:
        print("NO")