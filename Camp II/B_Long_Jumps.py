for _ in range(int(input())):
    input()
    arr = list(map(int,input().split()))
    start = len(arr)

    maxi = float("-inf")
    while start:
        start -= 1
        position = start + arr[start]
        if position < len(arr):
            arr[start] += arr[position]
        maxi = max(arr[start], maxi)
    print(maxi)

