class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        myUnion = UnionFind()

        for eq in equations:
            if eq[1] == '=':
                myUnion.union(eq[0], eq[-1])
        
        for eq in equations:
            if eq[1] == '!' and myUnion.find(eq[0]) == myUnion.find(eq[-1]):
                return False
        return True

class UnionFind:
    def __init__(self):
        self.parents = {}
        for i in range(26):
            self.parents[chr(ord('a')+i)] = chr(ord('a')+i)
            
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        repX, repY = self.find(x), self.find(y)

        if repX < repY:
            self.parents[repY] = repX
        else:
            self.parents[repX] = repY
