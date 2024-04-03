def solve():
    input()

    nums = list(map(int, input().split()))
    lett = list(input())

    for i in range(len(lett)):
        num = nums[i]
        for j in range(len(nums)):
            if nums[j] == num:
                nums[j] = lett[i]
    
    if  nums == lett:
        return "YES"
    else:
        return "NO"
            



for _ in range(int(input())):
    print(solve())