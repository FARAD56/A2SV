class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        ans = [-1,-1]
        while i < len(nums):
            if nums[i]-1 != i:
                if nums[nums[i]-1] == nums[i]:
                    ans[0] = nums[i]
                    ans[1] = i+1
                    i+=1
                else:
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1
        return ans