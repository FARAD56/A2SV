class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.size = {}
        self.min_max = {}

        for i in range(1, n+1):
            self.parents[i] = i
            self.size[i] = 1
            self.min_max[i] = (i,i)

    def get(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.get(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        repX, repY = self.get(x), self.get(y)

        x_min, x_max = self.min_max[repX]
        y_min, y_max = self.min_max[repY]

        if repX != repY:
            if self.size[repX] < self.size[repY]:
                self.parents[repX] = repY
                self.size[repY] += self.size[repX]
                self.min_max[repY] = (min(x_min,y_min),max(x_max,y_max))
            else:
                self.parents[repY] = repX
                self.size[repX] += self.size[repY]
                self.min_max[repX] = (min(x_min,y_min),max(x_max,y_max))


n, m = map(int, input().split())
myUnion = UnionFind(n)

for _ in range(m):
    query = input()
    

    if query[0] == 'u':
        x,y = map(int,query[5:].split())
        myUnion.union(x,y)
    else:
        x = int(query[4])
        repX = myUnion.get(x)
        print(*myUnion.min_max[repX],myUnion.size[repX])

