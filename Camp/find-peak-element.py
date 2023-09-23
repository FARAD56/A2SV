class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = nums + [float("-inf")] 
        l , r = 0, len(nums) -2
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid+1] > nums[mid] and nums[mid+1] > nums[mid-1]:
                l = mid + 1
            else:
                r = mid -1

        return l


            
        