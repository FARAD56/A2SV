from math import ceil
def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    if nums == sorted(nums) and len(nums) > 2:
        return ceil(len(nums)/2)

    stack1 = []
    nextGreater1 = [-1]*len(nums)

    for i in range(len(nums)):

        while stack1 and nums[stack1[-1]] < nums[i]:
            stackTop = stack1.pop()
            nextGreater1[stackTop] = i
        
        stack1.append(i%len(nums))

    diff = []

    for i in range(len(nums)):
        if nextGreater1[i] > 0:
            diff.append(nextGreater1[i]-i)

    print(nextGreater1)
    print(diff)
    
    diff += [0,0]
    diff.sort
    return diff[-1] + diff[-2]

t = int(input())

for _ in range(t):
    print(solve())