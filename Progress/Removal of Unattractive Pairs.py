from collections import Counter
def solve():
    n = int(input())
    word = input()
    count = Counter(word)
    count = count.most_common()

    if len(word) < 2 * count[0][1]:
        print(2*count[0][1]- len(word))
    elif len(word) > 2*count[0][1]:
        print(len(word)%2)
    else:
        print(0)

    


t = int(input())
for _ in range(t):
    solve()