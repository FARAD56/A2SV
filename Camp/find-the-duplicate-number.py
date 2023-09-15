class Solution:
    def search(self,nums,target):
        l , r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return True
        return False

    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        num = 1
        n = len(nums)
        while num <= n-1:

            left, right = bisect_left(nums,num), bisect_right(nums,num)
            if (right != left + 1) and self.search(nums,num) == True:
                return num
            num += 1