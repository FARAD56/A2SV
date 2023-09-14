class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float("-inf")] + nums + [float("-inf")] 
        l , r = 1, len(nums) -2
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid-1
            elif nums[mid+1] > nums[mid] and nums[mid+1] > nums[mid-1]:
                l = mid + 1
            else:
                r = mid -1

        return l-1


            
        