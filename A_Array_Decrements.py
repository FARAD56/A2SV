def solve():
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = set()
    p1,p2 = [],[]
    zeros = float("-inf")
    for i in range(n):
        if a[i] < b[i]:
            return "NO"
            
        elif a[i] > b[i]:
            if b[i] == 0:
                zeros = max(zeros, a[i]-b[i])
                
            else:
                ans.add(a[i]-b[i])


        if len(ans) > 1:
            return "NO"

    if ans and zeros > min(ans):
        return "NO"

    return "YES"


t = int(input())

for _ in range(t):
    print(solve())