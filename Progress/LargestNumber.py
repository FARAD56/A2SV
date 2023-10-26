class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(key=lambda x: (x * 9),reverse=True)
        largest_num = "".join(nums)
        if largest_num[0] == '0':
            return '0'
        return largest_num
        