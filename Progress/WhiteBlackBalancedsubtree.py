from collections import defaultdict
import sys, threading

def main():
    t = int(input())
    
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        Dict = defaultdict(list)
        colors = input()
        color_Dict = {'W' : -1, 'B':1}
        
        for idx,num in enumerate(nums):
            Dict[(num,color_Dict[colors[num-1]])].append((idx+2,color_Dict[colors[idx+1]]))
            
        
        count = 0
        def dfs(root):
            nonlocal count
            if not Dict[root]:
                return root[1]
            
            result = root[1]
            for neighbour in Dict[root]:
                result += dfs(neighbour)
                
            
            if result == 0:
                count += 1
            return result

        dfs((1,color_Dict[colors[0]]))
        print(count)    
    
 
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    

