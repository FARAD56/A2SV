class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagicSquare(subgrid):
            # Check if all numbers from 1 to 9 are present
            nums = set(num for row in subgrid for num in row)
            if nums != set(range(1, 10)):
                return False
            
            # Calculate the sum of each row, column, and diagonal
            target_sum = sum(subgrid[0])
            
            for i in range(1, 3):
                if sum(subgrid[i]) != target_sum:
                    return False
            
            for j in range(3):
                if sum(subgrid[i][j] for i in range(3)) != target_sum:
                    return False
            
            if subgrid[0][0] + subgrid[1][1] + subgrid[2][2] != target_sum:
                return False
            
            if subgrid[0][2] + subgrid[1][1] + subgrid[2][0] != target_sum:
                return False
            
            return True
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [grid[x][j:j+3] for x in range(i, i+3)]
                if isMagicSquare(subgrid):
                    count += 1
        
        return count