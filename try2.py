nums = [1,13,10,12,31]
new_num = []
for num in nums:
    num = int(str(num)[::-1])
    new_num.append(num)
nums += new_num

ans = len(set(nums))
print(ans)