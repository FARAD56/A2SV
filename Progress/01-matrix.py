class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        soln = []

        queue = deque()
        for i in range(len(mat)):
            val = []
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    val.append(0)
                    queue.append((i,j))
                else:
                    val.append(-1)
            soln.append(val)
        
        print(soln)
                    


        while queue:
            r,c = queue.popleft()

            for rm,cm in directions:
                if 0<=r+rm < len(mat) and 0<=c+cm<len(mat[0]) and soln[r+rm][c+cm] == -1:
                    soln[r+rm][c+cm] = soln[r][c] + mat[r+rm][c+cm]
                    queue.append((r+rm,c+cm))

        return soln
        
        
        
        
        
        

