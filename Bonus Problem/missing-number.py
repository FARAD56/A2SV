class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.append(-1)
        ans = len(nums)+1
        while i < len(nums):
            if nums[i] != i:
                if nums[i] == -1:
                    ans = i
                    i+=1
                else:
                    nums[nums[i]] , nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        return nums.index(-1)