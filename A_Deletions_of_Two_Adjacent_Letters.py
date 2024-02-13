for _ in range(int(input())):
    a = input()
    b = input()

    ind = []

    check = True
    if b in a:
        for i in range(len(a)):
            if a[i] == b:
                ind.append(i)

        for num in ind:
            if not num%2:
                print("YES")
                check = False
                break
    if check:
        print("NO")
