''' 
if even then you get only one move
if odd, two moves
start from end and decrease down while ensuring even
'''


n,m=map(int,input().split())
s = 0

while n<m:
    if m%2 == 0:
        s += 1
    else:
        m += 1
        s += 2

    m //= 2

    

print(int(s+n-m))