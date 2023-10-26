n = int(input())
 
array = list(map(int, input().split()))
 
odd_count, even_count = 0,0
for num in array:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
if even_count > 0 and odd_count > 0:
    array.sort()
 
print(*array)