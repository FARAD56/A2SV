class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def dp(l, r, turn):
            if l > r: return 0

            if (l,r, turn) not in memo:
                if not turn: memo[(l,r,turn)] = max(dp(l+1, r, True)+ nums[l], dp(l, r-1, True) + nums[r])
                else: memo[(l,r,turn)] = min(dp(l+1, r, False)- nums[l], dp(l, r-1, False)- nums[r])
            return memo[(l,r, turn)]
        memo = {}
        return 0 <= dp(0, len(nums)-1, False)





            