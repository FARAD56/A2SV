from collections import OrderedDict

N = int(input())

diction = OrderedDict()
list1 = []

for i in range(N):
    inpt = input().split()
    if len(inpt) > 2:
        inpt[0] = inpt[0] + " " + inpt[1]
        inpt.remove(inpt[1])
    inpt[1] = int(inpt[1])
    list1.append(inpt)
    
for item in list1:
    if item[0] in diction:
        diction[item[0]] += item[1]
    else:
        diction[item[0]] = item[1]

for key, value in diction.items():
    print(key, value)