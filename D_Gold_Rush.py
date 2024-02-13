for _ in [*open(0)][1:]:
    n,m=map(int,_.split())
    result = True
    for i in range(25):
        for j in range(i, 25):
            if 3**j * m == 2**i * n:
                result = False
                break

    if not result:
        print('YES')
    else:
        print('NO')
