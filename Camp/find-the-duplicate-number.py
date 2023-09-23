class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0,len(nums)-1

        while l <= r:
            mid = l + (r-l)//2

            count = sum([1 for num in nums if num <= mid])

            if count > mid:
                r = mid - 1
            else:
                l = mid + 1

        return l
