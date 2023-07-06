t = int(input())

def checkDescend(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            continue
        else:
            return 'YES'
    return 'NO'

ans_list = []
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    ans = checkDescend(nums)
    ans_list.append(ans)
    
for ans in ans_list:
    print(ans)
    