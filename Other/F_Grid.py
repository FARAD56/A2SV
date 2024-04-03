maxi = 1
for _ in range(21):
    n = input()
    ones = n.split('0')
    zeros = n.split('1')

    for arr in ones:
        maxi = max(maxi, len(arr))

    for arr in zeros:
        maxi = max(maxi, len(arr))


print(maxi+1)
