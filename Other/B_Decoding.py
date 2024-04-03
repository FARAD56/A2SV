n = int(input())

arr = input()[::-1]
n = len(arr)

ans = ['' for _ in range(len(arr))]

val = 1 if n %2 else 0

if val:
    ans[n//2] = arr[-1]

r, l = len(arr)-1, 0
for i in range(0,len(arr)-val,2):
    ans[r], ans[l] = arr[i], arr[i+1]
    r -= 1
    l += 1
    

    
print(''.join(ans))





