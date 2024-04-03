num = int(input())
n_bit = num.bit_length()-1

n = 0
check = 0
while n < num:

    if not check: val = "NO"
    if check: val = "YES"

    for _ in range(n_bit-1):
        print(val)

    check = 1-check

    n += n_bit-1

