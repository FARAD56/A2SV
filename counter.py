# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

X = int(input())

shoe_sizes = input().split()
shoe_sizes = Counter(shoe_sizes)
number_of_customers = int(input())

money_earned = 0

for i in range(number_of_customers):
    inpt = input().split()
    for key in shoe_sizes:
        if inpt[0] == key:
            if shoe_sizes[key] > 0:
                shoe_sizes[key] -=1
                money_earned += int(inpt[1])
            else:
                pass

print(money_earned)
    

    
