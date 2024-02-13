from collections import deque
n, k = map(int, input().split())

board = []
for _ in range(2):
    board.append(list(input()))

queue = deque([(0,0)])
direction = [(1,k),(0,1),(-1,k),(0,-1)]

visited = set()
while queue:
    r, c = queue.popleft()
    if c + k >= len(board[0]):
        print("YES")
        exit()

    for rm, cm in direction:
        if c + cm < len(board[0]) and 0 <= r+rm < 2 and board[r+rm][c+cm] == "-" and (r+rm,c+cm) not in visited:
            visited.add((r+rm, c+cm))
            queue.append((r+rm, c+cm))
print("NO")


