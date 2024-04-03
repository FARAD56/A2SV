for _ in range(int(input())):
    n = int(input())

    ans = ''
    
    for i in range(9,0,-1):
        if n >= i:
            ans += str(i)
            n -= i

    print(int(ans[::-1]))
    