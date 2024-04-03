from collections import defaultdict
for _ in range(int(input())):
    n = int(input())

    nums = list(map(int, input().split()))

    arr = input()

    ones = [nums[i] for i in range(len(nums)) if arr[i]=='1']

    zeros = [nums[i] for i in range(len(nums)) if arr[i]=='0']

    ones.sort()
    zeros.sort()

    Dict = defaultdict(int)

    zeros += ones


    for i in range(len(nums)):
        Dict[zeros[i]] = i+1

    ans = []
    for num in nums:
        ans.append(Dict[num])
    print(*ans)
