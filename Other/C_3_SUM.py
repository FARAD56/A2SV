from collections import defaultdict
for i in range(int(input())):
    input()
    nums = list(map(int,input().split()))
    remainders = []

    Dict = defaultdict(int)
    for num in nums:
        if Dict[num%10] < 3:
            Dict[num%10] += 1
            remainders.append(num%10)
    
    goal=True
    for i in range(len(remainders)):
        for j in range(i+1,len(remainders)):
            for k in range(j+1,len(remainders)):
                if(remainders[i]+remainders[j]+remainders[k])%10==3:
                    if goal:print("YES")
                    goal=False
                    break
    if goal:print("NO")

