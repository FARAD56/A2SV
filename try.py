deadends = ["0201","0101","0102","1212","2002"]
arr, target = [],'2222'
value = "0000"
for i in range(4):
    ref = list(value)
    if ref[i] < target[i]:
        ref[i] = str(int(ref[i])+1)
        ref = ''.join(ref)
        if ref not in deadends:
            arr.append(ref)

print(arr)