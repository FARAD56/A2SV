from collections import Counter
def solve():
    input()
    counts = Counter(list(map(int, input().split())))
    new = dict()

    for count in counts:
        if counts[count] % 2:
            new[count] = 1


    

    if len(new) > 1:
        return "YES"
    else:
        return "NO"



for _ in range(int(input())):
    print(solve())