class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0]*len(height)
        maxi = 0
        for i in range(len(height)-1,-1,-1):
            maxi = max(maxi, height[i])
            water[i] = maxi

        maxi = ans = 0

        for i in range(len(height)):
            maxi = max(maxi, height[i])
            ans += min(maxi, water[i]) - height[i]
        
            
        return ans
            
