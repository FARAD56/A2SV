class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = float("-inf")

        val = [num for num in satisfaction if num > 0] 
        if not val: return 0

        for i in range(len(satisfaction)):
            val = satisfaction[i:]
            sam = 0
            for j in range(len(val)):
                sam += val[j]*(j+1)
            ans = max(sam,ans)
        return ans

            
