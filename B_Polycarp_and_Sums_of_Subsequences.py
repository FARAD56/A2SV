def solve():
    nums = list(map(int, input().split()))

    jump = -1
    for i in range(1, 4):
        if nums[i]+nums[i-1] == nums[i+1]:
            jump = i + 1
            break
    
    ans = nums[:4]
    ans = [nums[i] for i in range(len(ans)) if i != jump]
    print(*ans[:3])


t = int(input())

for _ in range(t):
    solve()