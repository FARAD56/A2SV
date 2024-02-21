class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def Sum(idx, sum_):
            if idx == len(nums):
                return int(sum_ == target)

            if (idx, sum_) not in memo:
                memo[(idx, sum_)] = Sum(idx+1, sum_- nums[idx]) + Sum(idx+1, sum_ + nums[idx])
            return memo[(idx, sum_)]

        memo = {}
        return Sum(0,0)

        
