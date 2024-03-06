class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        myUnion = UnionFind(len(edges))
        for u,v in edges:
            if myUnion.find(u) == myUnion.find(v):
                return [u,v]
            myUnion.union(u,v)

class UnionFind:
    def __init__(self,n):
        self.parents, self.size = {}, {}

        for i in range(n):
            self.parents[i+1] = i+1
            self.size[i+1] = 1

    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        repX, repY = self.find(x), self.find(y)

        if repX != repY:
            if self.size[repX] > self.size[repY]:
                self.parents[repY] = repX
                self.size[repX] += self.size[repY]
            else:
                self.parents[repX] = repY
                self.size[repY] += self.size[repX]
