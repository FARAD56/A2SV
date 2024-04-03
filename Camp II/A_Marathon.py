for _ in range(int(input())):
    nums = list(map(int, input().split()))
    count = sum([1 for num in nums if num > nums[0]])
    print(count)