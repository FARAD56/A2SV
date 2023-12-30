def solve():
    nums = input()

    if int(nums[-1]) %2 == 0:
        return 0

    if int(nums[0])%2 == 0:
        return 1

    check = False
    for i in nums:
        if int(i) % 2 == 0:
            return 2
    return -1

    



t = int(input())
for _ in range(t):
    print(solve())