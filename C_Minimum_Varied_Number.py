t = int(input())

for _ in range(t):
    num = int(input())

    ans = ''
    i =  9
    while num > i:
        num -= i
        ans += str(i)
        i -= 1    

    if num > 0:
        ans += str(num)
    print(ans[::-1])
