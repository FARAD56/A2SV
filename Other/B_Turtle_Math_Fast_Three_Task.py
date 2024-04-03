def solve():
    input()
    arr = list(map(int, input().split()))
    total = sum(arr)

    if total % 3 == 2:
        return 1
    elif total % 3 == 0:
        return 0
    else:
        for i in range(len(arr)):
            if arr[i] % 3 == 1:
                return 1
                
        return 2

for _ in range(int(input())):
    print(solve())