class Solution(object):

    import numpy as np

    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # base cases
        # target = 0, return 0
        # target = nums[0] return 1
        #
        # set length to infinit  i.e. float('inf')
        # use a sliding window..start with a pointer on the right...and move it..
        # sum we are looking for is sume += nums[right]
        # while summ >= target
        # calculate min length( length, right-left+1)
        # subtract the value pointed to by left
        # increment left...basically move the left pointer until the sum is less than target and then add the next right value
        # sum of input numbers < target
        # return(0)
        # if sum of input numbers == target
        # return len(nums)
        # return the calculated minimum length

        length = float('inf')
        left = 0
        summ = 0

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                length = min(length, right-left+1)
                summ-=nums[left]
                left+=1

        
        if sum(nums)<target:
            return(0)
        elif sum(nums)==target:
            return(len(nums))
        else:
            return(length)