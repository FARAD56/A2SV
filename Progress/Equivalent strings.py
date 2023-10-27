first, second = input(), input()

mem = {}
def comp(first, second):
    n,m = len(first),len(second)
    if (first, second) in mem:
        return mem[(first,second)]
    
    if n % 2 == 1:
        return first == second
        
    first1, first2 , second1,second2 = first[:(n//2)],first[(n//2):],second[:(m//2)],second[(m//2):]
    
    mem[(first,second)] = (comp(first1,second1) and  comp(first2,second2)) or (comp(first2,second1) and  comp(first1,second2))
    return mem[(first,second)]


if comp(first,second):
    print("YES")
else:
    print("NO")
    
        
     


    
