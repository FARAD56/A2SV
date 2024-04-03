comb =[0]+[10**9]*7

for y in range(int(input())):
    num , chars = input().split()
    num = int(num)
    sum_ = 0

    for char in chars:
        sum_ += 1<<(ord(char) - ord("A"))
    chars = sum_

    for i in range(8):
        comb[i|chars] = min(comb[i|chars],comb[i]+num)

if comb[7] == 10**9:
    comb[7]=-1
print(comb[7])