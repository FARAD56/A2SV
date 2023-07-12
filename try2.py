sequence = "ababc"
word = list("ba")
outer_count = 0
s = list(sequence)
for i in range(len(s)-1):
    if s[i] == word[0]:
        inner_count = 1
        for j in range(1,len(word)):
            if word[j] == s[i+j]:
                inner_count += 1
            else:
                break
        if inner_count == len(word):
            outer_count += 1
print(outer_count)