class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        zeros = nums.count(0)

        nums = [number for number in nums if number != 0]

        for i in range(zeros):
            nums.append(0)

        return nums