records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])

grades = set(record[1] for record in records)
second_lowest = sorted(grades)[1]

second_lowest_holder = [record[0] for record in records if record[1] == second_lowest]

second_lowest_holder.sort()
for holder in second_lowest_holder:
    print(holder)