from collections import defaultdict
import sys, threading


def main():
    n,m = map(int, input().split())
    
    amount = list(map(int, input().split()))

    Dict = defaultdict(list)
    for _ in range(m):
        src, dest = map(int, input().split())
        Dict[src].append(dest)
        Dict[dest].append(src)

    visited = set()
    
    def dfs(vertex,visited,mini):
        if vertex in visited:
            return mini
        
        if amount[vertex-1] < amount[mini]:
            mini = vertex-1
            
        visited.add(vertex)
        
        for neighbour in  Dict[vertex]:
            if neighbour not in visited:
                a = dfs(neighbour, visited,mini)
                if amount[a] < amount[mini]:
                    mini = a
        return mini
                

    total = 0
    for i in range(1,n+1):
        if i not in visited:
            a = dfs(i,visited,i-1)
            total += amount[a]
            
    print(total)
    
 
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    

