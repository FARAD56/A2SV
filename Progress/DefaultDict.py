# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

inpt = input().split()

n,m = int(inpt[0]), int(inpt[1])

groupA = []
groupB = []
for i in range(n):
    groupA.append(input())

for i in range(m):
    groupB.append(input())



for let in groupB:
    track = []
    for i in range(len(groupA)):
        if let == groupA[i]:
            track.append(i+1)
    if len(track) == 0:
        track.append(-1)
    print(*track)
            
            