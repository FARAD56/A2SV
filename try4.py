n = int(input())

cost = list(map(int, input().split()))
arr = sorted(cost)


t = int(input())
for i in range(t):
    print(arr,cost)
    p,l,r = map(int, input().split())
    
    if p == 2:
        for i in range(l-1,r):
            total += arr[i]
    else:
        for i in range(l-1,r):
            total += cost[i]
        
        
    

