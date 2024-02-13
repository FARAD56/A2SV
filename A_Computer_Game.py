for _ in range(int(input())):
    int(input())
    input_1 = map(int, input())
    input_2 = map(int, input())

    result = 'NO'
    for x, y in zip(input_1, input_2):
        if x != 0 and y != 0:
            result = 'NO'
            break
    else:
        result = 'YES'

    print(result)
