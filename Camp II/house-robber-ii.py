class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        def rob(n, arr, memo):
            if n in memo:
                return memo[n]

            if not n:
                return arr[n]

            if n == 1:
                return max(arr[0], arr[1])

            if n not in memo:
                memo[n] = max(arr[n] + rob(n - 2, arr, memo), rob(n - 1,arr, memo))
            return memo[n]

        memo1, memo2 = {}, {}
        a = rob(len(nums)-2, nums[:-1], memo1)
        b = rob(len(nums)-2, nums[1:], memo2)

        return max(a,b)
