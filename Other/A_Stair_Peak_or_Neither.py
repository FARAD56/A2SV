for _ in range(int(input())):
    arr = list(map(int, input().split()))

    if arr[0] < arr[1] < arr[2]:
        print("STAIR")
    elif arr[0] < arr[1] > arr[2]:
        print("PEAK")
    else:
        print("NONE")