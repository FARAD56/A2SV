def solve():
    n = int(input())
    max_bit = n.bit_length()

    val = (2**(max_bit-1))-1
    print(val)

for _ in range(int(input())):
    solve()