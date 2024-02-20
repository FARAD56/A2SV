class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def part(idx, target):
            if idx >= len(nums) or target <= 0:
                return 0 == target

            if (idx, target) not in memo:
                memo[(idx,target)] = part(idx + 1, target- nums[idx]) or part(idx+1, target)
            
            return memo[(idx, target)]
        
        memo = {}
        return sum(nums) % 2 == 0 and part(0, sum(nums)//2)