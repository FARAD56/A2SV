shifts = [[1,2,1],[2,3,1],[1,3,1]]

diff = [0]*5

for start, end , num in shifts:
    diff[start] += num
    diff[end+1] -= num

pre_sum = [diff[1]]
for i in range(2,4):
    pre_sum.append(pre_sum[-1]+ diff[i])

print(pre_sum)


