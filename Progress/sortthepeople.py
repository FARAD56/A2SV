class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        Dict = {}
        for i in range(len(names)):
            Dict[heights[i]] = names[i]
        
        heights.sort(reverse = True)
        ans = []
        for height in heights:
            ans.append(Dict[height])
        
        return ans