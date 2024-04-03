from math import gcd
def solve():
    mini, maxx = map(int, input().split())
    
    if not maxx%mini:
        return maxx*maxx//mini
    else:
        return maxx*mini//gcd(mini,maxx)

t = int(input())

for _ in range(t):
    print(solve())


