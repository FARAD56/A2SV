for _ in range(int(input())):
  a=int(input())
  print(a-(a%7)+7 if a%10<a%7 else a-(a%7))