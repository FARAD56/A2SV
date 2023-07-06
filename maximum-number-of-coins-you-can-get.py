class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        num = len(piles)/3
        piles.sort()
        print(piles)
        total = 0
        for i in range(num,len(piles),2):
            total += piles[i]
        return total