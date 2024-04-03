def solve(n):
    if n < 3:
        return n+1

    dp = [0 for _ in range(n+1)]

    dp[0], dp[1], dp[2] = 1, 2, 3

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%(1000000007)

    return dp[-1]

arr = input()

if 'm' in arr or 'w' in arr:
    print(0)
    exit()

upd = arr[0] if arr[0] == 'u' or arr[0] =='n' else ''
for i in range(1,len(arr)):
    if arr[i] == 'u' and arr[i-1] == 'u' or arr[i] == 'n' and arr[i-1] == 'n': upd += arr[i]
    elif arr[i] == 'u' and arr[i-1] != 'u' or arr[i] == 'n' and arr[i-1] != 'n': upd += ' ' + arr[i]
    else: upd += ' '

arr = upd.split()

ans = 1
for char in arr:
    ans *= solve(len(char)-1)

print(ans%(1000000007))
