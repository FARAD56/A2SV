from collections import defaultdict,deque
n,m = map(int,input().split())
nums = list(map(int,input().split()))

Dict = defaultdict(list)
for _ in range(n-1):
    src, dest = map(int,input().split())
    Dict[src-1].append(dest-1)
    Dict[dest-1].append(src-1)
    

queue = deque([(0,nums[0])])
visited = [0]*(n+1)
visited[0] = 1
ans = 0
while queue:

    root,color = queue.popleft()
    if color > m:
        continue

    valid = False

    for neighbour in Dict[root]:
        if visited[neighbour] == 0:
            visited[neighbour] = 1
            valid = True

            if nums[neighbour] == 1:
                queue.append((neighbour,color+1))
            else:
                queue.append((neighbour,0))
    if not valid:
        ans += 1

print(ans)

