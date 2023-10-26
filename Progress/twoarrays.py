t = int(input())

for i in range(t):
    n = int(input())

    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))

    a1.sort()
    a2.sort()

    for i in range(len(a1)):
        if a1[i] == a2[i]:
            continue
        else:
            a1[i] += 1
            
    if a1 != a2:
        print("NO")
    else:
        print("YES")



    