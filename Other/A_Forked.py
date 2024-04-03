def solve():
    x,y = map(int, input().split())
    k = list(map(int, input().split()))
    q = list(map(int, input().split()))

    if x + y == (sum(k)+sum(q)):
        return 2
    if sum(q) == sum(k) and x == y:
        return 1
    else:
        return 0





t = int(input())
for _ in range(t):
    print(solve())