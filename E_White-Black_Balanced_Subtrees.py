from collections import defaultdict
from collections import defaultdict
import sys, threading

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        children = list(map(int, input().split()))
        colors = input()
        graph = defaultdict(list)
        color_dict = {"W":-1, "B":1}

        for idx,num in enumerate(children):
            graph[(num, color_dict[colors[num-1]])].append((idx+2, color_dict[colors[idx+1]]))

        count = 0
        def dfs(parent):
            nonlocal count
            if not graph[parent]:
                return parent[1]

            result = parent[1]
            for child in graph[parent]:
                result += dfs(child)
            
            if not result: count += 1 
            return result
        
        dfs((1,color_dict[colors[0]]))
        print(count)

    

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()