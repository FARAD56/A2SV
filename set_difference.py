# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

english_roll = set(input().split())

X = int(input())

french_roll = set(input().split())

english_only = english_roll.difference(set(french_roll))

print(len(english_only))