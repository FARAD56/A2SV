t = int(input())
input_list = []
for i in range(t):
    N = int(input())

    nums = []
    total = 0
    for i in range(1,N+1):
        nums.append(i)
        total += i


    def calculate_total(nums):
        total = 0
        nums[0] += 1
        for i in range(len(nums)):
            total += nums[i]
        return total

    while total % N != 0:
        total = calculate_total(nums)

    input_list.append(nums)

for num in input_list:
    print(*num)
