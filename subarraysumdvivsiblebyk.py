from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        window = defaultdict(int)
        window[0] = 1
        curr = ans = 0

        for right in range(len(nums)):
            curr += nums[right]
            ans += window[curr % k]
            window[curr%k] += 1
        
        return ans