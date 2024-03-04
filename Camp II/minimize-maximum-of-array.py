class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        ans = 0

        for idx,num in enumerate(nums):
            total += num
            ans = max(ans, total/(idx+1))
        return ceil(ans)
