n = int(input())

nums = list(map(int, input().split()))

r, m, p = [],[],[]

for idx, num in enumerate(nums):
    if num == 1:
        r.append((idx,num))
    elif num == 2:
        m.append((idx, num))
    else:
        p.append((idx,num))

mini = min(min(len(r),len(m)),len(p))
print(mini)
ans = []
for i in range(mini):
    print(r[i][0]+1,m[i][0]+1,p[i][0]+1)
    

    