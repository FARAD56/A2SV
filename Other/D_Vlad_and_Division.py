from collections import Counter, defaultdict
for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))

    arr.sort()

    l, r = 0, len(arr)-1

    count = 0
    while l < r:
        if (arr[l] + arr[r]) == 2147483647:
            r -= 1
            l +=1
            count += 1
        elif (arr[l]+arr[r]) > 2147483647:
            r -= 1
        else:
            l +=1

    
    print(count + (len(arr)-(count*2)))
    
