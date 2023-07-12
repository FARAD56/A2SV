t = int(input())
 
for i in range(t):
    N, k = map(int, input().split())
    
    array = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if (array[i]-i-1) % k == 0:
            continue
        count += 1
        
    if count == 0:
        print(0)
    elif count <= 2:
        print(1)
    else:
        print(-1)
            