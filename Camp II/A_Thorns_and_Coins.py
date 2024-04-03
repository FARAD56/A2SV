for _ in range(int(input())):
    input()

    road = input()

    coins = 0
    for i in range(len(road)):
        if road[i] == '*' and i < len(road)-1 and road[i+1] == '*':
            break
        elif road[i] == '@':
            coins += 1

    print(coins)
    
            


