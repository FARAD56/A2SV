class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        if k > len(nums):
            for i in range(len(nums)):
                ans.append(-1)
        else:
            for i in range(k):
                ans.append(-1)

            for j in range(0,len(nums)-(2*k)):
                sliced = nums[j:(2*k+1+j)]
                total = sum(sliced)
                average = total/(2*k+1)
                ans.append(average)
            
            for i in range(len(nums)-k,len(nums)):
                ans.append(-1)
        return ans

solution = Solution()
solution.getAverages