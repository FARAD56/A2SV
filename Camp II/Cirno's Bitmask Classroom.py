def solve():
    n = int(input())

    if n == 1: return 3
    elif n%2 and n > 1: return 1
    else:
        if (2**(n.bit_length()-1)) == n:
            return n +1
        else:
            return n&((n-1)^(2**(n.bit_length())-1))

for _ in range(int(input())):
    print(solve())
        
            

        
