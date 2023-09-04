class Solution(object):
    def countWays(self, ranges):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """
        ranges.sort()
        count, bundles = 1, [float("-inf")]
        for start, end in ranges:
            if start <= bundles[-1]:
                bundles[-1] = max(bundles[-1], end)
            else:
                count = (count*2)% (10**9+7)
                bundles = [start,end]
        return count