for _ in range(int(input())):
    n = int(input())

    board = []

    for i in range(n):
        board.append(input().count("1"))

    board = [num for num in board if num]

    if len(set(board)) == 1:
        print("SQUARE")
    else:
        print("TRIANGLE")




