t = int(input())
ans_list = []
for i in range(t):
    array = list(map(int, input().split()))
    
    max_dist = abs(array[0] - array[1]) + abs(array[1] - array[2]) + abs(array[0] - array[2])
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                value = abs((array[0]+i)-(array[1]+j)) + abs((array[0]+i)-(array[2]+k)) + abs((array[2]+k)-(array[1]+j))
                if value < max_dist:
                    max_dist = value
                
    ans_list.append(max_dist)
    
for ans in ans_list:
    print(ans)