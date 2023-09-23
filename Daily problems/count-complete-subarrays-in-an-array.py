class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        m = len(set(nums))
        n = len(nums)
        count = 0
        for i in range(n):
            sub = set()
            for j in range(i,n):
                sub.add(nums[j])
                if len(sub) == m:
                    count += 1
        
        return count




        