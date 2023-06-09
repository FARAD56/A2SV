fruits = ('Mango','Pineapple', 'Banana')

# Unpack tuples
x, Y = (10,19)

x , y, *z  = (10,11),(2,4),(2,4),(2,4),(2,4)
r = list(x)
r.append(y)
r.append(set(z))
print(r)

y = 2

from math import sqrt
def countPrimes( n):
        """
        :type n: int
        :rtype: int
        """
        if 0 <= n <= 5 *(10**6): 
            prime_count = 0
            for j in range(2,n):
                flag = 0
                for i in range(2, int(sqrt(j)+1)):
                    if j % i == 0:
                        flag = 1
                        break
                if flag == 0:
                    prime_count += 1

        return prime_count


print(countPrimes(20))


N = int(input())

student = []
student_list = []

for i in range(N):
    student = []
    name = input()
    grade = float(input())
    student_list.append([name,grade])

print(student_list)

student_list.sort(key = lambda inside:inside[1])
print(student_list)

final_list = []

for i in range(0,N):
    if i + 1 > N:
        if (student_list[i+1][1]) == (student_list[i][1]):
            final_list.append(student_list[i])

print(final_list)