from collections import Counter

t, k = map(int,input().split())

ans = 0
for _ in range(t):
    count = set(list(input()))
    check = True

    for i in range(k+1):
        if str(i) not in count:
            check = False
    
    if check: ans += 1

print(ans)
