#User function Template for python3

class Solution: 
    # def select(self, arr, i):
    #     # code here 
    def selectionSort(self, arr,n):
        #code here
        # 4,1,3,9,7
        
        for i in range(n):
            min_index = i #4
            for j in range(i+1,n):
                if arr[j]<arr[min_index]:#1<4
                    min_index=j #min_index=1
            #swap 1 with 4
            arr[i],arr[min_index] = arr[min_index],arr[i]
            
        return arr
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends