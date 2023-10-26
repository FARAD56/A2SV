class NumMatrix(object):

    def __init__(self, matrix):
        self.pre_matrix = [[0 for col in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]

        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.pre_matrix[i][j] = self.pre_matrix[i][j-1] + self.pre_matrix[i-1][j] + matrix[i-1][j-1] - self.pre_matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        total = self.pre_matrix[row2+1][col2+1]
        return total - self.pre_matrix[row2+1][col1] - self.pre_matrix[row1][col2+1] + self.pre_matrix[row1][col1]