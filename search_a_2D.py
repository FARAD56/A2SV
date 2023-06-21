class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        count = 0
        for item in matrix:
            if target in item:
                count += 1
            else:
                continue
        if count > 0:
            return True
        else:
            return False