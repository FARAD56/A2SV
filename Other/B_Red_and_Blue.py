for _ in range(int(input())):
    r , b = 0,0

    input()
    red = list(map(int,input().split()))
    input()
    blue = list(map(int,input().split()))

    s = 0
    for x in red: 
        s += x; r = max(r, s)

    s = 0
    for x in blue: 
        s += x; b = max(b, s)

    print(r+b)
