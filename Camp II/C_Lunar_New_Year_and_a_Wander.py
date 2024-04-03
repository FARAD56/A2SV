from collections import defaultdict
from heapq import heapify, heappop, heappush
n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    src, dest = map(int, input().split())

    graph[src].append(dest)
    graph[dest].append(src)


stack = [1]
heapify(stack)
visited = set()
ans = []

while stack:
    node = heappop(stack)

    if node in visited:
        continue
    visited.add(node)
    ans.append(node)

    for child in graph[node]:
        if child not in visited:
            heappush(stack, child)


print(*ans)
