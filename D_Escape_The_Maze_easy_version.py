from collections import defaultdict, deque
def solve():
    empty = input()
    n, k = map(int, input().split())

    blocked = list(map(int,input().split()))
    graph = defaultdict(list)

    for i in range(n-1):
        src, dest = map(int, input().split())

        graph[src].append(dest)
        graph[dest].append(src)
    
    rooms = []
    queue = deque([(1,0)])

    visited = set()

    while queue:
        node, level = queue.popleft()

        if level == 1:
            rooms.append(node)
        if level > 1:
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, level+1))
                visited.add(neighbour)

    ans = []
    for room in rooms:
        check = False
        for friend in blocked:
            if friend in graph[room] or friend == room:
                check = True 
        if check == False:
            ans.append(room)
    
    if ans:
        return "YES"
    else:
        return "NO"
        
        

        



t = int(input())

for _ in range(t):
    print(solve())