for _ in range(int(input())):
    n , k = map(int, input().split())

    arr = [ord(char)-ord("a") for char in input()]

    for i in range(len(arr)-1):
        if arr[