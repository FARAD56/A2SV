t = int(input())

for _ in range(t):
    array = input()
    one = two = three = -1

    l = 0
    r= 0
    min_len = len(array) +1
    while r < len(array):
        if array[r] == '1':
            one = r
        elif array[r] == '2':
            two = r
        elif array[r] == '3':
            three = r
        r += 1
        if one != -1 and two != -1 and three != -1:
            l = min(one,two,three)
            min_len = min(min_len,r-l)
    if min_len > len(array):
        print(0)
    else:
        print(min_len)

        