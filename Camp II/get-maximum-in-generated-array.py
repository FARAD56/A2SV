class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]
        for i in range(n+1):
            if i < 2: dp[i] = i
            else:      
                if i % 2: dp[i] = dp[i//2] + dp[i//2 +1]
                else: dp[i] = dp[i//2]
        return max(0, max(dp))

         