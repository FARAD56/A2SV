t = int(input())

for i in range(t):
    n = int(input())
    
    array = list(map(int, input().split()))
    
    i, j = array.index(max(array))+1, array.index(min(array))+1

    print(j , i)