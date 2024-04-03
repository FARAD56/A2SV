def solve():
    n, k = map(int, input().split())

    health = list(map(int, input().split()))
    distance = list(map(int, input().split()))

    arrn = []
    for i in range(n):
        arrn.append(abs(distance[i])+ health[i])

    arrn.sort()
    
    sum_ = 0
    for i in range(len(arrn)):
        sum_ += k
        if sum_ - arrn[i] < 0: return "NO"
        sum_ += arrn[i]
    return "YES"



for _ in range(int(input())):
    print(solve())