if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command = input().split()
        if command[0] == 'insert': 
            arr.insert(int(command[1]),int(command[2]))
        if command[0] == 'remove': 
            arr.remove(int(command[1]))
        if command[0] == 'append': 
            arr.append(int(command[1]))
        if command[0] == 'sort': 
            arr.sort()
        if command[0] == 'pop': 
            arr.pop()
        if command[0] == 'reverse': 
            arr.reverse()
        if command[0] == 'print': 
            print(arr)