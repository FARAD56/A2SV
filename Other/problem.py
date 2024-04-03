from collections import defaultdict
input()

nums = list(input())

for idx,char in enumerate(nums):
    if char == '0':
        nums[idx] = -1
    else:
        nums[idx] = 1

dic = defaultdict(list)

curr = 0
ps = []
dic[0] = [-1]

for idx,num in enumerate(nums):
    curr += num
    dic[curr].append(idx)

ans = 0
for key in dic:
    ans = max(ans, dic[key][-1]-dic[key][0])
print(ans)

