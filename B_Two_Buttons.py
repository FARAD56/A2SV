from collections import deque
start, end = map(int, input().split())

if end <= start:
    print(start-end)
    exit()

queue = deque([start])
visited = set([start])
count = 0
while queue:
    start = queue.popleft()

    if end%start:
        if (start-1) not in visited:
            count += 1
            queue.append(start-1)
            visited.add(start-1)
    elif end%start == 0 and end != start:
        if (start*2) not in visited:
            count += 1
            queue.append(2*start)
        
    
print(count)
