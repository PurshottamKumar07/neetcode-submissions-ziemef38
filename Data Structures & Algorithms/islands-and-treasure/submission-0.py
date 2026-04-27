class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])

        def bfs(r,c):

            que=deque()
            que.append((r,c))

            while que:
                r,c=que.popleft()
                d=[[-1,0],[0,-1],[1,0],[0,1]]
                
                for i,j in d:
                    nr=r+i
                    nc=c+j
                    if nr>=m or nc>=n or nr<0 or nc<0 or grid[nr][nc]==-1:
                        continue
                    elif grid[nr][nc]<=grid[r][c]+1:
                        continue
                    else:
                        grid[nr][nc]=grid[r][c]+1 
                        que.append((nr,nc)) 

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    bfs(i,j)