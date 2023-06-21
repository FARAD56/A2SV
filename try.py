t = int(input())

for i in range(t):
    N = int(input())
    line = list(map(int, input().split()))

    not_good = True
    while not_good:
        track = 0
        for i in range(1,len(line)-1):
            count =0
            if line[i] % line[i-1] == 0 or line[i-1] % line[i] == 0:
                pass
            else:
                left_minimum,idx = min(line[i],line[i-1]),line.index(min(line[i],line[i-1]))
                left_maximum = max(line[i],line[i-1])
                back_mod = left_maximum % left_minimum
                # print('back_mod',back_mod,left_minimum)
                left_minimum += back_mod

                right_minimum,idx2 = min(line[i+1],line[i]),line.index(min(line[i+1],line[i]))
                right_maximum = max(line[i+1],line[i])
                front_mod = right_maximum % right_minimum
                # print('front_mod',front_mod,right_minimum)
                right_minimum += front_mod

                line[idx] = left_minimum
                line[idx2] = right_minimum
                count += 1
                track += 1
        
        left_minimum1, idx3 = min(line[0], line[-1]), line.index(min(line[0], line[-1]))
        left_maximum1 = max(line[0], line[-1])
        last_mod = left_maximum1 % left_minimum1
        left_minimum1 += last_mod
        # print('last_mod',last_mod,left_minimum1)
        line[idx3] = left_minimum1

        if track == 0:
            not_good = False
    
    print(*line)




