for _ in range(int(input())):
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))

    nums.sort(key = lambda x: x%k)

    l, r = 0, len(nums)-1

    pairs = []
    while l < r:
        if (nums[r]+nums[l])//k > (nums[r]//k + nums[l]//k):
            pairs += [l,r]
            r -= 1
        l += 1

    Set_pairs = set(pairs)
    pairs += [i for i in range(n) if i not in Set_pairs]

    count = 0
    for i in range(0,len(nums),2):
        count += (nums[pairs[i]]+nums[pairs[i+1]])//k

    print(count)

