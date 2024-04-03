for _ in range(int(input())):
    input()
    arr = input()

    if '...' in arr:
        print(2)
    else:
        print(arr.count('.'))