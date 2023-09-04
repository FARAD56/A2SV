class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        def good(value):
            r,count = len(nums)-1,0
            for l in range(len(nums)):
                while l < r and nums[r]+nums[l] > value:
                        r -= 1
                count += max(0,r-l)
            return count
        
        nums.sort()
        return good(upper) - good(lower-1)
