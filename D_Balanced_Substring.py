from collections import defaultdict

n=int(input())
x=list(input())

for idx,char in enumerate(x):
    if char == '0':
        x[idx] = -1
    else:
        x[idx] =1

dic = defaultdict(list)
dic[0].append(-1)
curr = 0
ps = [0]
for idx,num in enumerate(x):
    curr += num
    ps.append(curr)
    dic[curr].append(idx)

maxx = 0

for key in dic:
    maxx = max(dic[key][-1]- dic[key][0], maxx)

print(maxx)

