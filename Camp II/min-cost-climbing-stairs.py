class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        memo = {}
        def MCCS(n):

            if n in memo: return memo[n]
            if n < 2: return cost[n]
            result = min(cost[n]+ MCCS(n-1), cost[n]+MCCS(n-2))
            memo[n] = result
            return result

        return MCCS(len(cost)-1)