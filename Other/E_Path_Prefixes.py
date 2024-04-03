from collections import defaultdict, deque
def solve():
    graph = defaultdict(list)
    path = defaultdict(list)
    path[1] = [-1,0]

    n = int(input())
    for i in range(2,n+1):
        par, a, b = map(int, input().split())
        path[i] = [a,b]
        graph[par].append(i)

    queue = [(1, 0, 0, 0, 0)]

    ans = [0 for i in range(n-1)]
    while queue:
        node, level, a_sum, b_sum, par_max = queue.pop()

        if node != 1 and (path[node][0] >= path[node][1] or a_sum >= b_sum):
            par_max += 1

        print(node, par_max)
        if node > 1:
            ans[node-2] = par_max 

        for child in graph[node]:
            queue.append((child, level + 1, a_sum + path[child][0], b_sum + path[child][1], par_max))

    print(*ans)





for _ in range(int(input())):
    solve()