class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        maxx = 0
        Dict = defaultdict(int)
        for r in range(len(s)):
            Dict[s[r]] += 1
            while (r-l+1) > len(Dict):
                Dict[s[l]] -= 1
                if Dict[s[l]] == 0:
                    del Dict[s[l]]
                l += 1
            maxx = max(maxx, r-l+1)
        return maxx

            

        