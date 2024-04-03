for _ in range(int(input())):
    input()
    a = 0
    for val in input().split():
        a += abs(int(val))
    print(a)