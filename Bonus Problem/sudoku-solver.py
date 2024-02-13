class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(i,j,num,board):
            for row in range(9):
                if board[row][j] == num: return False

            for col in range(9):
                if board[i][col] == num: return False

            startRow = (i//3)*3
            startCol = (j//3)*3
            for row in range(startRow, startRow+3):
                for col in range(startCol, startCol+3):
                    if board[row][col] == num: return False

            return True
            
            
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':

                        for num in range(1,10):
                            if valid(i,j,str(num),board):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve()




            




                    

        