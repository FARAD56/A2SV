class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        myUnion = UnionFind(isConnected)

        n = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and myUnion.find(i+1)!=myUnion.find(j+1):
                    n -= 1
                    myUnion.union(i+1,j+1)
        return n



class UnionFind:
    def __init__(self, isConnected):
        self.parents = {}
        self.size = {}
        for i in range(len(isConnected)):
            self.parents[i+1] = i+1
            self.size[i+1] = 1
        
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)

        if u != v:
            if self.size[u] > self.size[v]:
                self.parents[v] = u
                self.size[u] += self.size[v]
            else:
                self.parents[u] = v
                self.size[v] += self.size[u]

        

