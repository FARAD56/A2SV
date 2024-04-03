for t in range(int(input())):
    n=int(input())
    s=input()
    tree=[list(map(int,input().split())) for _ in range(n)]
    res=n
    q=[(1,0)]
    while q:
        node, cnt = q.pop()
        l,r=tree[node-1]

        if l+r==0:
            print(cnt)
            res=min(res,cnt)
            continue

        if l:
            val = 1
            if s[node-1] == "L":
                val -= 1
            q.append((l,cnt+val))
        if r:
            val = 1
            if s[node-1] == "R":
                val -= 1
            q.append((r,cnt+val))


    print(res)

    
