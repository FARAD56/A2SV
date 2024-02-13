n , m = map(int, input().split())

board = []
for i in range(n):
    board.append(input())

keys = ["B","W"]
    
for i in range(n):
    arr = ""
    for j in range(m):
        if board[i][j] == "-":
            arr += "-"
        else:
            arr += keys[(i+j)%2]
    print(arr)

