class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target+1)]
        dp[-1] = 1
        for i in range(target, -1, -1):
            for num in nums:
                if i + num <= target: dp[i] += dp[i+num]

        return dp[0]

            
