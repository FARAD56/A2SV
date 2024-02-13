edges = [['s','a'], ['s','d'], ['a','b'],['a','d'],['d','e'],['b','c'],['e','f'],['f','g'],['b','e']]
from collections import defaultdict, deque

graph = defaultdict(set)

for x,y in edges:
    graph[x].add(y)
    graph[y].add(x)

stack = [(['s'],'s')]

while stack:
    path, node = stack.pop()

    lis = []
    for neighbour in graph[node]:
        if neighbour not in path:
            lis.append(neighbour)
            stack.append((path + [neighbour], neighbour))
            if neighbour == 'g':
                exit()
    print(node, '->', lis)