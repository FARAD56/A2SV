def solve():
    a, b = map(int, input().split())

    highest = a if a > b else b

    if a == b:
        return "Bob"

    if highest == a:
        if not (a-b) % 2:
            return "Bob"
        else:
            return "Alice"
    else:
        if not (b-a)%2:
            return "Bob"
        else:
            return "Alice"


t = int(input())

for _ in range(t):
    print(solve())