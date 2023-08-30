t = int(input())

for _ in range(t):
    s= list(input())
    new = set()

    if len(s) == 1:
        print(s[0])
    else:
        left , right = 0,0

        while right < len(s):
            if s[left] == s[right]:
                right += 1
            elif s[left] != s[right]:
                if (right - left) %2 != 0:
                    new.add(s[left])
                left = right
                right += 1
        if right == len(s):
            if (right-left) % 2 != 0:
                new.add(s[left])
        new = sorted(new)
        print(''.join(new))