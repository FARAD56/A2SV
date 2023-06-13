n = int(input())  # Number of elements in the array
array = list(map(int, input().split())) 
array.sort()

positives = []  # Set for positive numbers
zeros = []  # Set for zeros

# Divide the array into three sets
negatives = array[0]
array.pop(0)

zeros = [num for num in array if num == 0]

positives = [num for num in array if num != 0]

# Print the sets
print(1, negatives)
print(len(positives), *positives)
print(len(zeros), *zeros)
