class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(i,j,boolean):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or (i,j) in visited or grid[i][j] == '0':
                return boolean

            visited.add((i,j))
            boolean = True

            a = dfs(i+1,j,boolean) 
            b = dfs(i, j+1,boolean)
            c = dfs(i-1, j, boolean)
            c = dfs(i, j-1, boolean)

            return a or b or c or d



        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                boolean = False
                if grid[i][j] == '1':
                    ans = dfs(i,j,boolean)
                    if ans: 
                        count += 1
        print(visited)
        return count
