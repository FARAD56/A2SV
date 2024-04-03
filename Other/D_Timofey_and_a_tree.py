from functools import lru_cache
from collections import defaultdict

def bootstrap(f, stack=[]):
 from types import GeneratorType
 def wrappedfunc(*args, **kwargs):
  if stack:
   return f(*args, **kwargs)
  else:
   to = f(*args, **kwargs)
   while True:
    if type(to) is GeneratorType:
     stack.append(to)
     to = next(to)
    else:
     stack.pop()
     if not stack:
      break
     to = stack[-1].send(to)
   return to
 
 return wrappedfunc

n = int(input())

graph = defaultdict(list)

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b); graph[b].append(a)

colors = list(map(int, input().split()))

memo = {}

@bootstrap
def dfs(node, par):
    
    if (node, par) not in memo:
        for child in graph[node]:
            if par == child:
                continue
            if colors[node-1] != colors[child-1] or not (yield dfs(child, node)):
                memo[(node, par)] = False
        if (node, par) not in memo:
            memo[(node, par)] = True

    yield memo[(node, par)]
    
def solve():
    for key in graph:
        flag = True
        for child in graph[key]:
            flag &= dfs(child, key)
        
        if flag:
            print("YES") 
            print(key)
            return
    print("NO")  

solve()