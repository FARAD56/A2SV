from collections import defaultdict,deque
n,m = map(int,input().split())
nums = list(map(int,input().split()))

Dict = defaultdict(list)
for _ in range(n-1):
    src, dest = map(int,input().split())
    Dict[src].append(dest)
    Dict[dest].append(src)
    

queue = deque([(1,nums[0])])
visited = set([1])
ans = 0
while queue:

    root,color = queue.popleft()

    if color <= m:
        valid = False
        for neighbour in Dict[root]:
            if neighbour not in visited:
                visited.add(neighbour)
                valid = True

                if nums[neighbour-1] == 1:
                    queue.append((neighbour,color+1))
                else:
                    queue.append((neighbour,0))
                    
        if not valid: ans += 1

print(ans)

