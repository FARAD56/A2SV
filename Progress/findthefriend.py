class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        array = list(range(1, n + 1)) 
        current = 0 
        while len(array) > 1:
            idx = (current + k - 1) % len(array)
            array.pop(idx)
            current = idx % len(array)
        return array[0]
