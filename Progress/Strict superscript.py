# Enter your code here. Read input from STDIN. Print output to STDOUT

A = input().split()

n = int(input())

set_container = []
for i in range(n):
    newSet = input().split()
    set_container.append(newSet)

flag,total = 0,0
for new_set in set_container:
    total += len(new_set)
    for elem in new_set:
        for i in range(len(A)):
            if elem == A[i]:
                flag += 1

if flag == total:
    print("True")
else:
    print("False")
