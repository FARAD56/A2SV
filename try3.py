t = int(input())

for i in range(t):
    n = int(input())
    
    def check(n):
        if n < 9 and n != 2:
            return "NO"
        elif n==2:
            return "YES"
        for i in range(1,int(pow(n,0.5))):
            if n-(i**3) >= 0:
                if pow(n-(i**3),1/3) == float(pow(n-(i**3),1/3)):
                    if abs(int(pow(n-(i**3),1/3))) - pow(n-(i**3),1/3) < (1/10000000000):
                        return "YES"
        return "NO" 

    
    print(check(n))