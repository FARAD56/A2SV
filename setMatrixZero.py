class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        r_z = set()
        c_z = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    r_z.add(i)
                    c_z.add(j)
        for i in range(r):
            for j in range(c):
                if i in r_z or j in c_z:
                    matrix[i][j] = 0