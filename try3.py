def solve(arr,mx,mx2):
    results=[]
    for x in range(0,len(arr)):
        if arr[x]==mx:
            results.append(arr[x]-mx2)
            print(results)
        else:
            results.append(arr[x]-mx)
        return results

t=int(input())

for _ in range(t):
    n=int(input())
    array =list(map(int,input().split()))
    new_array =[num for num in array]
    new_array.sort()
    mx=new_array[n-1]
    mx2=new_array[len(array)-2]
    #print(mx,mx2)
    print(*solve(array,mx,mx2))

