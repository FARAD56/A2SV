class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        pre_sum = [0]* (len(s)+1)
        for i in reversed(range(len(s))):
            pre_sum[i] += (pre_sum[i+1]+ shifts[i])

        result = ''
        for i in range(len(shifts)):
            result += chr((((ord(s[i])-ord('a')) + pre_sum[i])%26) + ord('a'))
        return result