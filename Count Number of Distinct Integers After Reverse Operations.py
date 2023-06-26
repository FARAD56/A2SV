class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_num = []
        for num in nums:
            num = int(str(num)[::-1])
            new_num.append(num)
        nums += new_num

        ans = len(set(nums))
        return ans