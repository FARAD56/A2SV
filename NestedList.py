if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])

    records.sort(key = lambda x : x[1])

    for elem in records:
        if elem[1] == records[0][1]:
            records.remove(elem)

    print(records[1][0])
    for elem in records:
        if elem[1] == records[1][1]:
            print(elem[0])


        
    