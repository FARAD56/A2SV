def solve():
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))

    pro = 1
    for num in nums:
        pro*= num

    if 2023 % pro:
        print("NO")
    else:
        print("YES")
        ans = [2023 // pro]

        for _ in range(k-1):
            ans.append(1)
        print(*ans)






t = int(input())

for _ in range(t):
    solve()