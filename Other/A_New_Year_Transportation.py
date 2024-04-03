def solve():
    n, t = map(int, input().split())
    
    nums = list(map(int, input().split()))
    
    total = 1
    position = 0
    
    while total <= t:
        total += nums[position]
        if total == t:
            return "YES"
        position = total-1
        
    return "NO"
    

print(solve())

