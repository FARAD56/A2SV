N = int(input())

scores = input().split()

scores = [int(word) for word in scores]

min_value = scores[0]
max_value = scores[0]
count = 0
for number in scores:
    if number > max_value:
        count += 1
        max_value = number
    elif number < min_value:
        min_value = number
        count += 1

print(count)
