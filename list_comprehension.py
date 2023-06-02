x = int(input())
y = int(input())
z = int(input())
n = int(input())

arr1 = []
for i in range(x+1):
    arr1.append(i)

arr2 = []
for i in range(y+1):
    arr2.append(i)

arr3 = []
for i in range(z+1):
    arr3.append(i)

array = []
for i in arr1:
    for j in arr2:
        for k in arr3:
            if i + j + k != n:
                array.append([i, j, k])

print(array)