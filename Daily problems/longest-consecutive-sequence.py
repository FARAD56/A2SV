class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            new_num = []
            uni = {}
            new_num = [uni.setdefault(num,num) for num in nums if num not in uni]
            new_num.sort()
            l,r = 0,1
            max_length = 0
            while r < len(new_num):
                if (new_num[r] - new_num[r-1]) != 1:
                    max_length = max(max_length, r-l)
                    l = r
                r += 1
            max_length = max(max_length,r-l)
            return max_length
        else:
            return len(nums)
