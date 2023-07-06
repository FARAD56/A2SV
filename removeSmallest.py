t = int(input())

def check(array):
    for i in range(len(array)-1):
        if array[i+1] - array[i] <= 1:
            continue
        else:
            return 'NO'
    return 'YES'

ans_list = []

for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    ans = check(array)
    ans_list.append(ans)

for ans in ans_list:
    print(ans)

    