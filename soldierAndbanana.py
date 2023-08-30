n , k, w = map(int, input().split())

total = 0
for i in range(1,w+1):
    total += (n*i)

print(total - k)