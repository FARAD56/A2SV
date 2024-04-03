class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2

n,m = map(int, input().split())
lis = [list(map(int, input().split()))[1:] for _ in range(m)]

myUnion = UnionFind(n)
for arr in lis:
    if not arr:
        continue
    beg = arr[0]
    for num in arr[1:]:
        myUnion.union(beg, num)

print(*[myUnion.table[myUnion.find(i)] for i in range(n)])





