def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    odd = [nums[i] for i in range(len(nums)) if i % 2]
    even = [nums[i] for i in range(len(nums)) if not i%2]

    even_par , odd_par = 2,2
    if odd:
        odd_par = odd[0]%2
    if even:
        even_par = even[0]%2

    for num in odd:
        if num % 2 != odd_par:
            return "NO"

    for num in even:
        if num % 2 != even_par:
            return "NO"
    return "YES"

t = int(input())

for _ in range(t):
    print(solve())