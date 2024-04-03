from collections import defaultdict
n=int(input())
s=input() 
Dict = defaultdict(int)

for char in 'hard':
    Dict[char] = 0

cost= list(map(int,input().split()))
for i in range(n):
    if s[i]=='h':
        Dict['h']+=cost[i]
    if s[i]=='a':
        Dict['a']=min(Dict['a']+cost[i],Dict['h'])
    if s[i]=='r':
        Dict['r']=min(Dict['r']+cost[i],Dict['a'])
    if s[i]=='d':
        Dict['d']=min(Dict['d']+cost[i],Dict['r'])
print(Dict['d'])
    