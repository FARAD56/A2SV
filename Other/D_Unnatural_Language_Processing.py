t = int(input())
vowels = set(['a','e'])
cons = set(['b','c','d'])

for _ in range(t):
    n = int(input())
    word = input()

    r = 1

    temp = word[0]
    ans = ''
    while r < n:
        if word[r] in cons and word[r-1] in cons:
            temp += '.'
        temp += word[r]
        r += 1

    lis = temp.split('.')
    for idx,each in enumerate(lis):
        val = ''
        final = 0
        for i in range(0,len(each)-3,2):
            val += (each[i:i+2]+'.')
            final = i + 2
        val += each[final:]
        lis[idx] = val
    print('.'.join(lis))

    
