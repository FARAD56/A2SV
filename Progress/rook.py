def solve(char, num):
    for i in range(8):
        if chr(ord('a')+i) != char:
            print(chr(ord('a')+i) + num)
        
        if i+1 != int(num):
            print(char + str(i+1))

t = int(input())

for _ in range(t):
    char, num = list(input())
    solve(char, num)