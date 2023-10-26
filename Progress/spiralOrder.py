class Solution(object):
    def spiralOrder(self,matrix):
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        spiral = []

        while top <= bottom and left <= right:
            # Traverse from left to right
            for col in range(left, right + 1):
                spiral.append(matrix[top][col])
            top += 1

            # Traverse from top to bottom
            for row in range(top, bottom + 1):
                spiral.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left
                for col in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top
                for row in range(bottom, top - 1, -1):
                    spiral.append(matrix[row][left])
                left += 1

        return spiral
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = spiralOrder(matrix)
        return spiral