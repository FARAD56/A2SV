for _ in range(int(input())):
    s = input()
    ans = []
    low = []
    up = []
    for i in s:
        if i != 'b' and i != 'B':
            ans.append(i)
            if i in 'qwertyuiopasdfghjklzxcvbnm':
                low += [len(ans)-1]
            else:
                up += [len(ans)-1]
        if i == 'b':
            if len(low) >= 1:
                ans[low[-1]] = ''
                low.pop()
        if i == 'B':
            if len(up) >= 1:
                ans[up[-1]] = ''
                up.pop()
    print(''.join(ans))