for _ in range(int(input())):
    n = int(input())
    for i in range(2 * n):
        for j in range(n):
            if not (i // 2 + j) % 2:
                print('##', end="")
            else:
                print('..', end="")
        print()

