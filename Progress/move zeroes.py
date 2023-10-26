class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                right += 1
                left += 1
        print(nums)