class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        myUnion = UnionFind(grid)
        allowable = {
            1: {1,3,5},
            2: {2,5,6},
            3: {2,5,6},
            4: {1,2,3,5,6},
            5: {},
            6: {1,5,6}
        }

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                for rm, cm in [(0,1),(1,0)]:
                    if (rm,cm) == (0,1) and grid[r][c] == 2: continue
                    if 0 <= r+rm < len(grid) and 0 <= c+cm < len(grid[0]):
                        myUnion.union((r,c), (r+rm, c+cm), grid, allowable)

        return myUnion.find((0,0)) == myUnion.find((len(grid)-1,len(grid[0])-1))



class UnionFind:
    def __init__(self, grid):
        self.parents = {}
        self.size = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.parents[(i,j)] = (i,j)
                self.size[(i,j)] = 1

    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, pos1, pos2, grid, allowable):
        repA, repB = self.find(pos1), self.find(pos2)
        num1 = grid[pos1[0]][pos1[1]]
        num2 = grid[pos2[0]][pos2[1]]

        if repA != repB and (num2 in allowable[num1]):
            if self.size[repA] > self.size[repB]:
                self.parents[repB] = repA
                self.size[repA] += self.size[repB]
            else:
                self.parents[repA] = repB
                self.size[repB] += self.size[repA]

