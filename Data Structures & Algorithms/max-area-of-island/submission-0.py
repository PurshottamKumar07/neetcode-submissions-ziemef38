class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return 0
            
            area=1
            grid[i][j]=0

            dir=[[1,0],[-1,0],[0,1],[0,-1]]
            for w,q in dir:
                area+=dfs(w+i,q+j)
            return area
        
        for l in range(m):
            for k in range(n):
                if grid[l][k]==1:
                    ans=max(ans,dfs(l,k))
        return ans