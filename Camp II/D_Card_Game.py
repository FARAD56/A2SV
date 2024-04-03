for _ in range(int(input())):
    input()

    end = input()

    arr = input().split()

    end_move = [char for char in arr if char[1] == end]
    later = [char for char in arr if char[1]!= end]

    end_move.sort()
    later.sort(key = lambda x:x[1])
    later += end_move
    if not end_move:
        print("IMPOSSIBLE")
    else:
        for i in range(0,len(later),2):
            print(later[i], later[i+1])
