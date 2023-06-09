class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list = []
        for i in range(len(nums)+1):
            num = i 
            if num not in nums:
                return num