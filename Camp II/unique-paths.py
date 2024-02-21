class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path(r,c):
            if r== m-1 and c == n - 1:
                return 1

            if r >= m or c >= n:
                return 0

            if (r,c) not in memo:
                memo[(r,c)] = path(r+1,c) + path(r, c+1)
            
            return memo[(r,c)]
        
        memo = {}
        return path(0,0)

