t = int(input())

for _ in range(t):
    n = int(input()) - 6
    mid , beg, end = 3,2,1
    while n:
        mid += 1 ; n -= 1
        if n: beg += 1; n-= 1
        if n: end += 1; n-=1

    print(beg, mid, end)