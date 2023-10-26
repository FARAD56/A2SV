class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        cols = len(matrix[0])
        rows = len(matrix)
        
        mat = [[0 for _ in range(rows)] for _ in range(cols) ]

        for i in range(rows):
            for j in range(cols):
                mat[j][i] = matrix[i][j]

        return mat

        print(matrix)