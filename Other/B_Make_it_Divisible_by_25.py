for _ in range(int(input())):
    s = input()
    a=[];i=0

    while True:
        i = i - 1
        x = s[i]
        if x not in a:
            a += '05' * (x == '0') + '27' * (x == '5')
        else:
            break

 
    print(-i-2)