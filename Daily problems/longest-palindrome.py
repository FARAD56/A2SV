from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = Counter(s)
        print(len(s),count)
        counts ,total = 0,0
        for key in count:
            if count[key] % 2 == 0:
                total += count[key]
            else:
                total += (count[key] -1)
                counts += 1
        
        return total if counts == 0 else total + 1
