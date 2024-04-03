from bisect import bisect as br
R,G=lambda:map(int,input().split()),range;t,=R()
for _ in G(t):
  n,=R();g=[[] for _ in G(n)]
  for i in G(1,n):
    p,a,b=R();g[p-1]+=[(i,a,b)]
  r=[0]*(n);Pb=[0]*n;stk=[(0,0,0,0)]
  while stk:
    u,pa,ub,dep=stk.pop()
    Pb[dep]=0 if dep==0 else Pb[dep-1]+ub
    r[u]=dep if Pb[dep]<=pa else br(Pb,pa,hi=dep)-1
    for v,a,b in g[u]:stk+=[(v,pa+a,b,dep+1)]
  print(*r[1:])