t = int(input())

for i in range(t):
    rows,cols = map(int, input().split())
    grid = [list(input()) for _ in range(rows)]
    for col in range(cols):
        for _ in range(rows-1,-1,-1):
            for itr in range(rows-2,-1,-1):
                while grid[itr][col] == '*' and grid[itr+1][col]=='.':
                    grid[itr][col]= '.'
                    grid[itr+1][col]='*'
    
    for i in range(rows):
        print(''.join(grid[i]))


        