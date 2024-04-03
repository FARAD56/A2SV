def solve():
    n = int(input())

    nums = list(map(int, input().split()))
    nums= nums[::-1]

    Set = set()

    for num in nums:
        if num in Set:
            break
        Set.add(num)

    return len(nums)- len(Set)


t = int(input())

for _ in range(t):
    print(solve())