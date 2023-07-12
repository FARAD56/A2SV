target, number = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
if number == 0 and array[0] > 1:
    print(1)
elif number == 0 and array[0] == 1:
    print(-1)
elif number <= target-1:
    if array[number-1] != array[number]:
        print(array[number-1])
    else:
        print(-1)
elif number == target:
    print(array[number-1])




