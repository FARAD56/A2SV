class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        def dp(i , flag):

            if i == len(prices):
                return 0

            if (i, flag) not in memo:
                if not flag:
                    memo[(i,flag)] = max(dp(i+1,True)+prices[i]-fee, dp(i+1, False))
                else:
                    memo[(i, flag)] = max(dp(i+1, False)-prices[i], dp(i+1, True))

            return memo[(i,flag)]
        
        memo = {}
        return dp(0,True)