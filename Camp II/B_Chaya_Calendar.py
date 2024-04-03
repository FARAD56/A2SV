for _ in range(int(input())):
    input()

    arr = list(map(int, input().split()))

    ans = arr[0]

    for i in range(1,len(arr)):
        ans += (arr[i] -(ans%arr[i]))
    print(ans)