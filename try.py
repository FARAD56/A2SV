# n = int(input())
# k = int(input())

# arr = [i+1 for i in range(n)]
# new_list = []
# count = 0
# for i in range(0,k*n-1,k):
#     if i >= 0:
#         new_list.append(arr[i])
        
#     count = (count + 1) % len(arr)

# print(*new_list)

n = int(input())
k = int(input())


array = list(range(1, n + 1))  # Create a list of array
print(array)
current = 0  # Index of the current friend

while len(array) > 1:
    remove_index = (current + k - 1) % len(array)

    array.pop(remove_index)

    # Update the current index for the next iteration
    current = remove_index % len(array)

# Return the last remaining friend (the winner)
print(*array)
