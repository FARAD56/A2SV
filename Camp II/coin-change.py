class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def den(amount):
            if amount < 0: return float("inf")
            if not amount: return 0

            if amount not in memo:
                mini = float("inf")

                for coin in coins:
                    mini = min(mini, 1 + den(amount-coin))

                memo[amount] = mini
            
            return memo[amount]

        memo = {}
        solution = den(amount)
        return solution if solution != float("inf") else -1