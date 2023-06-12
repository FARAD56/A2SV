t = int(input())  # Number of test cases

for _ in range(t):
    a1, b1 = map(int, input().split())  # Dimensions of the first rectangle
    a2, b2 = map(int, input().split())  # Dimensions of the second rectangle

    # Check if it is possible to form a square
    if (a1 + a2 == max(b1, b2) and b1 == b2) or (a1 + b2 == max(b1, a2) and b1 == a2) or (b1 + a2 == max(a1, b2) and a1 == b2) or (b1 + b2 == max(a1, a2) and a1 == a2):
        print("YES")
    else:
        print("NO")
 