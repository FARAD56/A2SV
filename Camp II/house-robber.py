class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(n):
            if n in meme:
                return meme[n]
            if not n:
                return nums[n]
            if n == 1:
                return max(nums[0],nums[1])

            meme[n] = max(nums[n]+rob(n-2), rob(n-1))
            return meme[n]
        meme = {}
        return rob(len(nums)-1)