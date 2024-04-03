grid = []

for _ in range(int(input())):
    a = input()
    grid.append(a)

r , c = len(grid)//2, len(grid)//2

direction = [(1,1), (-1,-1), (-1,1), (1,-1)]

diagonals = set([(r,c)])
for i in range(1,len(grid)//2+1):

    for rm, cm in direction:
        rm *= i
        cm *= i

        if grid[r+rm][c+cm] != grid[r][c]:
            print("NO")
            exit()
        
        diagonals.add((r+rm, c+cm))

non_diagonal = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in diagonals:
            non_diagonal.add(grid[i][j])
    

if len(non_diagonal) > 1 or list(non_diagonal)[0] == grid[r][c]:
    print("NO")
else:
    print("YES")