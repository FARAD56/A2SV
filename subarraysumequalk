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
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1]+nums[i])

        count = 0

        for i in range(1,len(pre_sum)):
            count += win[pre_sum[i]-k]
            win[pre_sum[i]] += 1

            
        return count