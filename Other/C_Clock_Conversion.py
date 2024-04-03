for _ in range(int(input())):
    arr = list(map(int, input().split(':')))

    letter = 'AM' if arr[0] < 12 else 'PM'
    arr[0] += 12 if arr[0] != 12 else 0

    if arr[0]>= 13:
        arr[0] %= 12

    ans = '0'+str(arr[0]) if arr[0] < 10 else str(arr[0])
    ans += ':'
    ans += '0'+str(arr[1]) if arr[1] < 10 else str(arr[1])
    ans += ' ' + letter

    print(ans)
