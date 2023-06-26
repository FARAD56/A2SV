
n = len(arr)
ismountain = False
if n>=3:
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            ismountain = True
        elif arr[i]>arr[i+1]:
            ismountain = True
        else:
            ismountain = False
        
return ismountain