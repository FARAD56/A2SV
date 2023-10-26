n = int(input())
nums = list(map(int, input().split()))

nums.sort()
beg = 1

for num in nums:
    if num <= beg:
        beg += num
    else:
        break
    
print(beg)