I=lambda:sorted(map(int,input().split()))
n=I()[0]
a=I()
m=I()[0]
b=I()
i,j,k=0,0,0
while i<n and j<m:
	if abs(a[i]-b[j])<2:k+=1;i+=1;j+=1
	elif a[i]<b[j]:i+=1
	else:j+=1
print(k)