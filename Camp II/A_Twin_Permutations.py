for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    print(*[n- num + 1 for num in nums])