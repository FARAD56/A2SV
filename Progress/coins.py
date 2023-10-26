t = int(input())
ans = []
for i in range(t):
    n, k = map(int, input().split())
    if n%2 == 0 or n%k == 0 or (n-k)%2 == 0:
        ans.append('YES')
    else:
        ans.append('NO')

for an in ans:
    print(an)