n = int(input())
number = 2*n+1
array = []
for row in range(2*n+1):
    row1 = ' ' * abs(n-row) 
    for dig in range(min(row,2*n-row) +1):
        row1 += str(dig)
    row1+= row1[::-1]
    row1 = list(row1)
    row1.remove(row1[n])
    for i in range(len(row1)):
        if row1[-1] == ' ':
            row1.pop(-1)
    array.append(row1)
for item in array:
    print(*item)