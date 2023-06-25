from collections import Counter
n,m = map(int, input().split())
def count_occurrences(string):
    counts = Counter(string)
    return counts

col_matrix = [[] for _ in range(m)]
row_matrix = []
for i in range(n):
    string = list(input())
    for i in range(m):
        col = col_matrix[i]
        col.append(string[i])
        
    occurrences = count_occurrences(string)

    for j in range(len(string)):
        if occurrences[string[j]] > 1:
            string[j] = '0'
    row_matrix.append(string)

for i in range(len(col_matrix)):
    lis = col_matrix[i]
    occur = count_occurrences(lis)
    for j in range(len(lis)):
        if occur[lis[j]] > 1:
            lis[j] = '0'
    col_matrix[i] = lis

cols = len(col_matrix[0])
rows = len(col_matrix)

mat = [['0' for _ in range(rows)] for _ in range(cols) ]

for i in range(rows):
    for j in range(cols):
        mat[j][i] = col_matrix[i][j]

ans = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == row_matrix[i][j] and mat[i][j] != '0':
                ans.append(mat[i][j])
print(''.join(ans))