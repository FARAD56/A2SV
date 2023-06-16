
"""
An array b of m
positive integers is good if for all pairs i and j (1≤i,j≤m), max(bi,bj) is divisible by min(bi,bj).

You are given an array a of n positive integers.
You can perform the following operation:

Select an index i (1≤i≤n) and an integer x (0≤x≤ai) and add x
to ai, in other words, ai:=ai+x.
After this operation, ai≤10^18 should be satisfied.
You have to construct a sequence of at most n operations that will make a good.
It can be proven that under the constraints of the problem, such a sequence of operations always exists.

Input
Each test contains multiple test cases. The first line contains a single integer t
(1≤t≤104) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n
(1≤n≤105) — the length of the array a.

The second line of each test case contains n
 space-separated integers a1,a2,…,an (1≤ai≤109) — representing the array a.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test, output a single integer p
 (0≤p≤n) — denoting the number of operations in your solution.

In each of the following p lines, output two space-separated integers — i and x.
You do not need to minimize the number of operations. It can be proven that a solution always exists.
  """
t = int(input())

for _ in range(t):
    N = int(input())
    line = list(map(int, input().split()))

    is_good = False

    while not is_good:
        is_good = True

        for i in range(1, len(line)-1):
            if line[i] % line[i - 1] == 0 or line[i - 1] % line[i] == 0:
                continue

            left_minimum, idx = min(line[i], line[i - 1]), line.index(min(line[i], line[i - 1]))
            left_maximum = max(line[i], line[i - 1])
            back_mod = left_maximum % left_minimum
            left_minimum += back_mod

            right_minimum, idx2 = min(line[i + 1], line[i]), line.index(min(line[i + 1], line[i]))
            right_maximum = max(line[i + 1], line[i])
            front_mod = right_maximum % right_minimum
            right_minimum += front_mod

            line[idx] = left_minimum
            line[idx2] = right_minimum
            is_good = False

    print(*line)
