from collections import defaultdict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Dict = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            if Dict[nums[i]] > 1:
                nums[i] = "_"
                count += 1
            Dict[nums[i]] += 1
        
        l = r = 0
        while r < len(nums):
            if nums[r] == "_":
                r += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                l += 1
        
        return len(nums) - count

        