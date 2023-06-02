N = int(input())

names = input().split()
bad_names = input().split()

for bad in bad_names:
    for name in names:
        if bad == name:
            names.remove(name)

count_list = []           
for name in names:
    count = len(set(name))
    count_list.append(count)

flag = 0
for i in range(len(names)):
    if count_list[i] == len(names[i]):
        flag += 1

print(flag)