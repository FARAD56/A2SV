class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        new_mat = []
        total = []
        for item in mat:
            total += item
        if len(mat)*len(mat[0]) == r*c:
            new_mat = [total[i:i+c] for i in range(0, len(total), c)]
        else:
            new_mat = mat

        return new_mat

        


    