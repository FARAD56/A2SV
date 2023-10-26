t = int(input())

for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    l,r = 0,n-1
    new_array = []
    while l <= r:
        new_array.append(array[l])
        if l != r:
            new_array.append(array[r])
        l+= 1
        r-=1
    print(*new_array)
