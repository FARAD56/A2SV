from collections import Counter
def destroyer(array):
    counts = Counter(array)
    sorted_counts = dict(sorted(counts.items()))
    keyarr, valuearr = [],[]
    for key in sorted_counts:
        keyarr.append(key)
        valuearr.append(sorted_counts[key])
    
    if keyarr[0] != 0:
        return 'NO'
    
    
    for i in range(1,len(keyarr)):
        if (0 <= keyarr[i] - keyarr[i-1] <= 1) and (valuearr[i] <= valuearr[i-1]):
            continue
        else:
            return 'NO'
    return 'YES'
        
t= int(input())
ans_list = []
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans_list.append(destroyer(arr))

for ans in ans_list:
    print(ans)