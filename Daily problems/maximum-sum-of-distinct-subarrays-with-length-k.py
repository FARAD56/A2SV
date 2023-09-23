class Solution(object):
    def maximumSubarraySum(self, nums, k):
        win = set()
        max_sum = 0
        cur,left = 0,0
        for i in range(len(nums)):
            cur += nums[i]
            if (i-left+1) > k:
                win.remove(nums[left])
                cur -= nums[left]
                left +=1
            while nums[i] in win:
                win.remove(nums[left])
                cur -= nums[left]
                left +=1
            win.add(nums[i])
            if (i-left+1) == k:
                max_sum = max(max_sum,cur)
            

        return max_sum