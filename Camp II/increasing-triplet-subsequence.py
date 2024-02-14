class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = float("inf")

        if len(nums) < 3: return False

        for num in nums:
            if b < num > a: return True
            if num <= b: b = num
            else: a = min(a,num)
        return False