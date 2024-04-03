maxi = 0
ins = set()
for _ in range(int(input())):
    type, id = map(str, input().split())
    
    if type == "+":
        ins.add(id)
    else:
        if id not in ins:
            maxi += 1
        else:
            ins.remove(id)
    maxi = max(maxi, len(ins))

print(maxi)
    
    