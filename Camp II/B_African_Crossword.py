from collections import Counter, defaultdict
n, m = map(int, input().split())

board = []
for i in range(n):
    board.append(list(input()))

row_count = []
for row in board:
    row_count.append(Counter(row))

for row in range(n):
    for col in range(m):
        char = board[row][col]
        if row_count[row][char] > 1:
            board[row][col] = '_'

col_count = []

for col in range(m):
    Dict = defaultdict(int)
    for row in board:
        Dict[row[col]] += 1
    col_count.append(Dict)

for col in range(m):
    


