from collections import defaultdict
def solve():
    n = int(input())

    par = list(map(int, input().split()))
    order = list(map(int, input().split()))
    graph = defaultdict(int)
    
    for i in range(n):
        graph[order[i]] = i

    ans = []

    for i in range(n):
        val = graph[i+1] - graph[par[i]]
        ans.append(val)

    return ans if min(ans) == 0 else [-1]

    


for _ in range(int(input())):

    print(*solve())