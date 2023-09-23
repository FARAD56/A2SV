class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        left,right = [0],[0]*len(nums)
        ltotal, rtotal = 0,0
        for i in range(1,len(nums)):
            ltotal += nums[i-1]
            left.append(ltotal)

        for i in range(len(nums)-2,-1,-1):
            rtotal += nums[i+1]
            right.insert(0,rtotal)
        
        for i in range(len(nums)):
            ans.append(abs(right[i]-left[i]))
        return ans