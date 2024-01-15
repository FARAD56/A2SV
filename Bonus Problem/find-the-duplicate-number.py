class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i]-1 != i:
                if nums[nums[i]-1] == nums[i]:
                    return nums[i]
                nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        return len(nums)
