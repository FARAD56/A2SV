for _ in range(int(input())):
    n = int(input())
    p = 10**(n//2)
    for i in range(n//2):
        print((p+3*10**i)**2)
        print((3*p+10**i)**2)
    print((p+4*p//10)**2)