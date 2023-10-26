class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        point = 1
        for n in nums:
            ans.append(point)
            point *= n
        

        point =1
        for i in reversed(range(len(nums))):
            print(ans[i],point)
            ans[i] *= point
            point *= nums[i]

        return ans