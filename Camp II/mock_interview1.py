'''
Example 1
G = [[1,2],[1,3],[2,4],[3,4]], source = 1, destination = 4
Answer: [[1,2,4], [1,3,4]]

Example 2
G = [[1,2], [2,3],[3,4],[3,5],[5,6],[4,6],[6,7],[5,7]], source = 1, destination = 7
Answer = [[1,2,3,4,6,7],[1,2,3,5,6,7],[1,2,3,5,7],[1,2,3,4,6,5,7]]
'''
G = [[1,2], [2,3],[3,4],[3,5],[5,6],[4,6],[6,7],[5,7]]; source = 1; destination = 7

from collections import defaultdict

graph = defaultdict(list)

for u, v in G:
    graph[u].append(v)
    graph[v].append(u)

res = []

queue = []
queue.append((source, [source], set([source])))

i = 0
while queue:
    node, path, visited = queue.pop()
    i += 1
    if node == destination:
        res.append(path.copy())
    else:
        for child in graph[node]:
            if child not in visited:
                queue.append((child, path + [child], visited|{child}))
            
print(res)

    


