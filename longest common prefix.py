class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        for i in range(len(strs[0])):
            for word in strs:
                if len(word) == i or word[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix