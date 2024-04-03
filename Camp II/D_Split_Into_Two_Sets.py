# from collections import defaultdict
# class UnionFind:
#     def __init__(self, n):
#         self.parents = {}
#         self.size = {}

#         for i in range(1, n+1):
#             self.parents[i] = i
#             self.size[i] = 1

#     def get(self, x):
#         if x == self.parents[x]:
#             return x
#         self.parents[x] = self.get(self.parents[x])
#         return self.parents[x]
    
#     def union(self, x, y):
#         repX, repY = self.get(x), self.get(y)

#         if self.size[repX] < self.size[repY]:
#             self.parents[repX] = repY
#             self.size[repY] += self.size[repX]
#         else:
#             self.parents[repY] = repX
#             self.size[repX] += self.size[repY]

# def solve():
#     n = int(input())
#     myUnion = UnionFind(n)

#     check = False
#     for i in range(n):
#         a, b = map(int, input().split())
#         if a == b: check = True
#         myUnion.union(a,b)

#     par = defaultdict(list)

#     for i in range(1, n+1):
#         par[myUnion.get(i)].append(i)

#     for key in par:
#         if len(par[key])%2 == 1 or check:
#             return "NO"

#     return "YES"


# for _ in range(int(input())):
#     print(solve())


def solve():
    n = int(input())
    colors = [-1]*n

    for _ in range(n):
        