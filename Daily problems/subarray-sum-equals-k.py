from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        win = defaultdict(int)
        win[0] = 1
        count = 0
        curr = 0
        for num in nums:
            curr += num
            count += win[curr-k]
            win[curr] += 1

        return count
