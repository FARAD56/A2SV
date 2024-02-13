t=int(input())
for _ in range(t):
    n=int(input())
    a=[*map(int, input().split())]
    p,s=[0,0],0
    for i in a:
        s+=i
        p[i%2]+=1
        print(s-p[1]//3-(p[1]%3==1 and p[1]+p[0]>1))