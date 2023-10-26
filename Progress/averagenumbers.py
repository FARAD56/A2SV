
n = int(input())
 
array = list(map(int, input().split()))
total = 0
for number in array:
    total += number
 
count = 0
ans = []
for i in range(n):
    if array[i] == (total-array[i])/(n-1):
        ans.append(i+1)

        count += 1
    
print(count)
print(*ans)