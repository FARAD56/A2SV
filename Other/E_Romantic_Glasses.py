def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    Dict = {0:0,1:0}

    l = 0

    for r in range(len(nums)):
        Dict[r%2] += nums[r]

        while 



t = int(input())

for _ in range(t):
    print(solve())