class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        suf = sum(grid[0])
        pre = 0
        ans = float("inf")
        for i in range(len(grid[0])):
            suf -= grid[0][i]
            ans = min(ans, max(suf,pre))
            pre += grid[1][i]
        return ans