# Enter your code here. Read input from STDIN. Print output to STDOUT
inpt = input().split()
N = int(inpt[0])
X = int(inpt[1])


list1 = []
for _ in range(X):
    subject = input().split()
    list1 += [subject]

x = tuple(zip(*list1))

for tup in x:
    total = 0
    for i in range(X):
        total += float(tup[i])
    print(total/(X))
        
