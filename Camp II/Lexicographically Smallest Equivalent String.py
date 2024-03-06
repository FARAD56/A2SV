class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        myUnion = UnionFind()
        for i in range(len(s1)):
            myUnion.union(s1[i],s2[i])

        ans = ''
        for i in range(len(baseStr)):
            ans += myUnion.find(baseStr[i])
        return ans
        

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
