t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    l,r = 0,min(n,k)
    count = 0
    ans = 0
    while l <= r:
        mid = (l+r)//2
        if (n+k-(2*mid)) >= mid*2:
           ans = mid
           l = mid + 1
        else:
            r = mid -1
    print(ans)
        
        

    
    
    
        
     


    
