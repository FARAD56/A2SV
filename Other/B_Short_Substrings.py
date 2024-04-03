def solve():
    a = input()

    i = 1
    num = set()
    while i < len(a)-1:
        if a[i] == a[i+1]:
            num.add(i+1)
            i+=2
        else:
            i += 1
    
    b = [a[i] for i in range(len(a)) if i not in num]
    return "".join(b)

t = int(input())

for i in range(t):
    print(solve())
