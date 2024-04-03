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
myUnion = UnionFind(m)

count = 0
lan_set = set()
for _ in range(n):
    emp = list(map(int, input().split()))
    num, lan = emp[0], emp[1:]

    count += 0 if num else 1

    for lang in lan:
        lan_set.add(lang)

    for i in range(len(lan)-1):
        myUnion.union(lan[i], lan[i+1])


par = set()
a = list(myUnion.parents.keys())
for key in a:
    if key not in lan_set:
        del myUnion.parents[key]

for key in myUnion.parents:
    if key in lan_set:
        par.add(myUnion.get(key))

print(len(par)+count-1 if par else count)


