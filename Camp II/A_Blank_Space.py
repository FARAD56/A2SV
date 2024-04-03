

for i in range(int(input())):
    input()
    arr = input().split()

    maxi = 0
    count = 0

    for char in arr:
        if char == '0':
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    maxi = max(maxi, count)
    print(maxi)