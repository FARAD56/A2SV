t = int(input())

for _ in range(t):
    lis = list(map(int, input().split()))

    for num in lis:
        if lis.count(num) == 1:
            print(num)