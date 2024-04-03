for _ in range(int(input())):
    n, q = map(int, input().split())

    arr = list(map(int, input().split()))
    total = sum(arr)
    odd = sum(1 for num in arr if num%2)
    even = len(arr) - odd

    for _ in range(q):
        type , num = map(int, input().split())


        total += (odd*num) if type else (even*num)

        if num%2:
            even , odd = (len(arr), 0) if type else (0, len(arr))

        print(total)