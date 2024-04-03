def solve():
    n = int(input())
    maxx = 0
    for char in input():
        maxx = max(maxx, ord(char)-ord('a')+1)
    return maxx


t = int(input())

for _ in range(t):
    print(solve())