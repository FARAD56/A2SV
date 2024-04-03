from collections import Counter
for _ in range(int(input())):

    count = Counter(input())

    print(count.most_common()[0][0])