from collections import Counter
t = int(input())

for _ in range(t):
    board = ''

    for _ in range(3):
        board += input()

    count = Counter(board)

    for key in count:
        if count[key] == 2:
            print(key)