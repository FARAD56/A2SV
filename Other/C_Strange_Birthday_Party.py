for _ in range(int(input())):
    n,m = map(int, input().split())

    integers = [int(char)-1 for char in input().split()]

    costs = list(map(int, input().split()))

    integers.sort(reverse = True)

    sum_ = 0
    for i in range(len(integers)):
        sum_ += costs[min(i, integers[i])] 

    print(sum_)


# from math import ceil
# for _ in range(int(input())):
#     n,m = map(int, input().split())

#     integers = list(map(int, input().split()))

#     costs = list(map(int, input().split()))

#     integers.sort()

#     sum_ = 0

#     for i in range(ceil(n/2)):
#         sum_ += costs[i%len(costs)]


#     for i in range(n//2):
#         sum_ += costs[integers[i]-1]
    
#     print(sum_)


