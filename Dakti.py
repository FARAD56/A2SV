N = int(input())

ans_list = []

for i in range(N):

    stri = input().split()

    list1 = []
    diction = {}

    for word in stri:
        list1.append(list(word))


    for word in list1:
        let = ''
        for letter in word:
            if letter.isdigit():
                let += letter
        let = int(let)
        diction[let] = word

    dic = list(sorted(diction.items()))
    list1 =[]
    for word in dic:
        list1.append(word[1])

    new_list = []
    for word in list1:
        new_word = ''
        word = [char for char in word if not char.isdigit()]
        new_word = ''.join(word)
        new_list.append(new_word)
    
    ans_list.append(new_list)

for lists in ans_list:
    print(*lists)

    