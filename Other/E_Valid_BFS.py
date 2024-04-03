from collections import defaultdict, deque


n = int(input())

graph = defaultdict(set)
for _ in range(n-1):
    src, dest = map(int, input().split())

    graph[src].add(dest)
    graph[dest].add(src)

soln = list(map(int,input().split()))

i , j = 1,0

if soln[0] != 1:
    print("No")
    exit()

while (i<n and j < n):
    if soln[i] in graph[soln[j]]:
        i += 1
    else:
        j+=1

if i==n:
    print("Yes")
else:
    print("No")