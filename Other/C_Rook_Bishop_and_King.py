r1,c1, r2,c2 = map(int, input().split())

rook = (r1!=r2) + (c2!=c1)
king = max(abs(r1-r2),abs(c1-c2))

if abs(r1-r2) == abs(c1-c2):
    bishop = 1
elif not (abs(r1-r2)-abs(c1-c2))%2:
    bishop = 2
else:
    bishop = 0

print(rook, bishop, king)