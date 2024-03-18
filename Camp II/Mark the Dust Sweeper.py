for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().lstrip('0 ').split()))[:-1]
    print(sum(a)+ a.count(0))
    
