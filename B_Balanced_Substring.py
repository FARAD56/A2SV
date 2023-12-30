from collections import defaultdict
def solve():
    n = int(input())
    nums = list(input())

    ans = []
    for r in range(n):
        count = defaultdict(int)
        count['a'] = nums[r:].count('a')
        count['b'] = nums[r:].count('b')

        for j in range(n-1,r,-1):
            if count['a'] == count['b']:
                ans = [r+1,j+1]
                break
            count[nums[j]] -= 1
    
    if ans:
        print(*ans)
    else:
        print(-1,-1)





t = int(input())

for _ in range(t):
    solve()