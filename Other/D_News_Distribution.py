class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.size = [1]*(n+1)

    def get(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.get(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        repX, repY = self.get(x), self.get(y)

        if repX!=repY:
            if self.size[repX] <= self.size[repY]:
                self.parents[repX] = repY
                self.size[repY] += self.size[repX]
            else:
                self.parents[repY] = repX
                self.size[repX] += self.size[repY]

n, m = map(int, input().split())
myUnion = UnionFind(n)

for _ in range(m):
    query = list(map(int, input().split()))
    num, lis = query[0], query[1:]

    if not lis: continue

    for num in lis[1:]:
        myUnion.union(lis[0],num)

ans = [myUnion.size[myUnion.get(i+1)] for i in range(n)]

print(*ans)











