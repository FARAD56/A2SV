class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n % 2 != 0:
            n *= 2
        else:
            n = n
        
        return n