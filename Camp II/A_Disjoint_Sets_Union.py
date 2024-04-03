class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.size = {}

        for i in range(1, n+1):
            self.parents[i] = i
            self.size[i] = 1

    def get(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.get(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        repX, repY = self.get(x), self.get(y)

        if self.size[repX] < self.size[repY]:
            self.parents[repX] = repY
            self.size[repY] += self.size[repX]
        else:
            self.parents[repY] = repX
            self.size[repX] += self.size[repY]

n, m = map(int, input().split())
myUnion = UnionFind(n)

for _ in range(m):
    query, x, y = input().split()
    x,y = int(x), int(y)

    if query == 'union':
        myUnion.union(x,y)
    else:
        if myUnion.get(x) == myUnion.get(y):
            print("YES")
        else:
            print("NO")

