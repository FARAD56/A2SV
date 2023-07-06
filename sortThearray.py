n = int(input())
arr = list(map(int, input().split()))

# Find the leftmost and rightmost indices where the array is unsorted
left, right = None, None
for i in range(1, n):
    if arr[i] < arr[i-1]:
        left = i - 1
        break
else:
    # Array is already sorted
    print("yes")
    print("1 1")
    exit()

for i in range(n-2, -1, -1):
    if arr[i] > arr[i+1]:
        right = i + 1
        break

# Reverse the subsegment and check if the array becomes sorted
subsegment = arr[left:right+1]
reversed_subsegment = subsegment[::-1]
sorted_arr = arr[:left] + reversed_subsegment + arr[right+1:]

if sorted_arr == sorted(arr):
    print("yes")
    print(left+1, right+1)
else:
    print("no")
