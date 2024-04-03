from collections import Counter
n = int(input())

count = Counter(input().lower())
if len(count) == 26:
    print("YES")
else:
    print("NO")