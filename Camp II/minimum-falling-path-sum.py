class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def dp(r,c):
            if r == len(matrix) - 1 and 0 <= c < len(matrix[0]):
                return matrix[r][c]

            if r == len(matrix) or c == len(matrix[0]) or c < 0:
                return float("inf")

            if (r,c) not in memo:
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                    memo[(r,c)] = matrix[r][c] + min(dp(r+1,c-1), dp(r+1, c), dp(r+1, c+1))
                
            return memo[(r,c)]

        memo = {}
        ans = float("inf")

        for i in range(len(matrix[0])):
            ans = min(ans, dp(0,i))

        return ans