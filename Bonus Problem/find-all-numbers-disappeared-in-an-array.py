class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < len(nums):
            if nums[i]-1 != i:
                if nums[nums[i]-1] == nums[i]:
                    i+=1
                else:
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1
        return [i+1 for i in range(len(nums)) if nums[i]-1 != i]