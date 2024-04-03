target , num = map(int, input().split())

ans = [num]
while num > target:
    val = str(num)
    if int(val[-1]) == 1:
        num //= 10
    else:
        if num %2 == 0:
            num //= 2
        else:
            print("NO")
            exit()

    ans.append(num)

ans = ans[::-1]
if num == target:
    print("YES")
    print(len(ans))
    print(*ans)
else:
    print("NO")

    
