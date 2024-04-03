def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if k != 1 or sorted(arr)== arr:
        return "YES"
    else:
        return "NO"


for _ in range(int(input())):
    print(solve())