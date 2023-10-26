t = int(input())  # Number of test cases
 
for _ in range(t):
    input()  # Read the empty line before each test case
 
    # Read the chessboard
    chessboard = [input() for _ in range(8)]
 
    # Find the position of the bishop
    for row in range(1, 7):
        for col in range(1, 7):
            if chessboard[row][col] == '#' and chessboard[row-1][col-1] == '#' and chessboard[row-1][col+1] == '#' and chessboard[row+1][col-1] == '#' and chessboard[row+1][col+1] == '#':
                print(row + 1, col + 1)  # Output the row and column (adding 1 to convert to 1-indexing)
                break
        else:
            continue
        break