import sys, threading
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


def main():
    def solve():
        n, graph, graph, visited, num_of_children = int(input()), defaultdict(list), defaultdict(list), set([1]), defaultdict(int)

        for i in range(n-1):
            par, chd = map(int, input().split()); graph[par].append(chd) ; graph[chd].append(par)

        def get_children(root, par):
            children = []
            for child in graph[root]:
                if child == par:
                    continue
                children.append(child)
            return children

        @bootstrap
        def cal_node(root, par):
            if not get_children(root, par):
                yield 0
            for child in graph[root]: 
                if child == par:
                    continue
                num_of_children[root] += 1 + (yield cal_node(child, root))
            yield num_of_children[root]
    
        cal_node(1, 0)


        @bootstrap
        def dp(root, par):

            if not get_children(root, par): yield 0

            if root not in memo:
                if len(get_children(root, par)) == 2:
                    a = num_of_children[get_children(root, par)[0]] + (yield dp(get_children(root, par)[1], root))
                    b = num_of_children[get_children(root, par)[1]] + (yield dp(get_children(root, par)[0], root))
                    memo[root] = yield max(a,b)
                else:
                    memo[root] = num_of_children[get_children(root, par)[0]]
            yield memo[root]

            
        memo = {}
        return dp(1, 0)


    for _ in range(int(input())):
        print(solve())

main()