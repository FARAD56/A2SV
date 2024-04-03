ps = []
count = 0
for i in range(200000+1):
    for char in str(i):
        count += int(char)
    ps.append(count)

for _ in range(int(input())):
    n = int(input())
    print(ps[n])
        


    
    

    
