arr = input()
nums = [1-int(x) for x in input()]
k = int(input())

count = 0
Set = set()
for i in range(len(arr)):
    string = arr[i:]

    val = sum(nums[ord(char)-ord('a')] for char in string)

    r = len(string)-1

    while val > k and r > -1:
        val -= nums[ord(string[r]) - ord('a')]
        r -= 1

    while r > -1:
        if arr[i:i+r+1] not in Set:
            Set.add(arr[i:i+r+1])
        r -= 1

print(len(Set))