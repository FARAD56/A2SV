from collections import Counter, defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    count = defaultdict(int)

    for char in input():
        count[char] += 1

    print(abs(count['+'] - count['-']))