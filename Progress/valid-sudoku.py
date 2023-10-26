class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num in seen and num.isalnum():
                    return False
                else:
                    seen.add(num)

        for col in range(len(board[0])):
            seen = set()
            for row in board:
                if row[col] in seen and row[col].isalnum():
                    return False
                else:
                    seen.add(row[col])

        def grid(rs, cs):
            seen = set()
            for row in range(rs,rs+3):
                for col in range(cs,cs+3):
                    if board[row][col] in seen and board[row][col].isalnum():
                        return False
                    else:
                        seen.add(board[row][col])
        for i in range(0,7,3):
            for j in range(0,7,3):
                if grid(i,j) == False:
                    return False
                

        return True