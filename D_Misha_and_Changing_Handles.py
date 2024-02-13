t = int(input())

A = {}
for i in range(t):
    a,b = input().split()

    if a not in A:
        A[b] = a
    else:
        A[b] = A[a]
        del A[a]

print(len(A))
for char in A:
    print(A[char], char)

    