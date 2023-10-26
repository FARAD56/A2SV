class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total = 0
        for i in range(0,len(mat)):
            #adding primary diagonal
            total += mat[i][i]
            #
        for i in range (len(mat)):
            j = len(mat) - 1 - i
            total += mat[i][j]

        if len(mat) % 2 != 0:
            total -= mat[len(mat)//2][len(mat)//2]

        return total
            