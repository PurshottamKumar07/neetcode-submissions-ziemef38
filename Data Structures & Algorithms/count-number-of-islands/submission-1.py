class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])

        def dfs(grid,i,j):
            if i>=m or j>=n or i<0 or j<0:
                return 
            
            if grid[i][j]=="1":
                grid[i][j]="."

                dir=[[1,0],[0,1],[-1,0],[0,-1]]
                for f,s in dir:
                    dfs(grid,i+f,j+s)
        ans=0
        for l in range(m):
            for k in range(n):
                if grid[l][k]=="1":
                    ans+=1
                    dfs(grid,l,k)
        
        return ans