from collections import Counter
t= int(input())

for i in range(t):
    n = int(input())
    
    array = list(map(int, input().split()))
    ans_array = []
    sorted_counts = sorted(array)
    max_value = sorted_counts[-1]
    sec_max = sorted_counts[len(array) - 2]

    ans_array = [num-max_value if num != max_value else max_value-sec_max for num in array]
        
    print(*ans_array)
    

