for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = sum(list(map(int, input().split())))

    val = 0 if (not ans or ans%k>0) else -1
    print(ans//k + val)