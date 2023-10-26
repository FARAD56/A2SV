from collections import Counter
t = int(input())

for i in range(t):
    n,c = map(int, input().split())

    array = list(map(int, input().split()))
    counts = Counter(array)
    cost = 0
    for key in counts:
        if key < c:
            cost += counts[key]
        else:
            cost += c

    print(cost)