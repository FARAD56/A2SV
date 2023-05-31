class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix_list = []

        for i in range(len(strs[0])):
            if strs[0][i] == strs[1][i] and strs[0][i] == strs[2][i]:
                prefix_list.append(strs[0][i])

        return(prefix_list)