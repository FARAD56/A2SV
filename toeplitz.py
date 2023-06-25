class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        count = 0
        for i in range(len(matrix) -1):
            for j in range(len(matrix[0])-1):
                if matrix [i][j] == matrix[i+1][j+1]:
                    count+= 1

        target = (len(matrix)-1)*(len(matrix[0]) -1)

        if count == 0 and len(matrix[0]) == 1:
            return True
        if count == 0 and len(matrix) > 1:
            return False
        elif count == target:
            return True

