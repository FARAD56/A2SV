from collections import defaultdict,deque
n = int(input())
queue = deque()
graph = defaultdict(list)
for i in range(n):
    parent = int(input())

    if parent > 0:
        graph[parent].append(i+1)
    else:
        queue.append((i+1,1))

ans = float("-inf")
while queue:
    node, level = queue.popleft()
    ans = max(ans, level)

    for neighbour in graph[node]:
        queue.append((neighbour,level+1))

print(ans)