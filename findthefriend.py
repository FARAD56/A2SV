n,k = int(input()),int(input())
array = list(range(1,(n+1)))
current = 0
while len(array) > 1:
    remove_index = (current + k -1) % len(array)
    array.pop(remove_index)
    current = remove_index % len(array)
print(*array)
