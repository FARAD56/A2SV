N = int(input())
pattern_list = []
for i in range(N):
    pattern_list.append(list(input()))
intersect = []
if len(pattern_list) == 1:
    for item in pattern_list[0]:
        if item == '?':
            item = 'x'
        intersect.append(item)
else:
    count = 0
    for i in range(N-1):
        for j in range(len(pattern_list[0])):
            if i + 1 < len(pattern_list[0]):
                # if first element[0] == next element[0] == ?
                if pattern_list[i][j] == '?' and pattern_list[i+1][j] =='?':
                    value = 'x'
                    intersect.insert(j,value)
                    count += 1
                    #   a == b != ?
                elif pattern_list[i][j] == pattern_list[i+1][j]:
                    if pattern_list[i][j] != '?':
                        value = pattern_list[i][j]
                        intersect.insert(j,value) 
                        count += 1  
                        # ? in first element or ? in second element, insert not ?
                elif pattern_list[i][j] != pattern_list[i+1][j]:
                    if pattern_list[i][j] == '?':
                        value = pattern_list[i+1][j]
                        intersect.insert(j,value)
                        count += 1
                    elif pattern_list[i+1][j] == '?':
                        value = pattern_list[i][j]
                        intersect.insert(j,value)
                        count += 1
    if count == 0:
        for i in range(len(pattern_list[0])):
            intersect.append('?')
ans = ''
for i in range(len(intersect)):
    ans += intersect[i]

print(ans)



                





