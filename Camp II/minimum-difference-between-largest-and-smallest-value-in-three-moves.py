class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0

        nums.sort()
        diff = nums[-1] - nums[0]
        move = len(nums) - 4
        for i in range(move, len(nums)):
            diff = min(diff, nums[i] - nums[i-move])
        
        return diff


        