class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        myUnion = UnionFind(n)
        for u,v in edges:
            myUnion.union(u,v)
        
        return myUnion.find(source) == myUnion.find(destination)


class UnionFind:
    def __init__(self,n):
        self.parents, self.size = {}, {}

        for i in range(n):
            self.parents[i] = i
            self.size[i] = 1

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
