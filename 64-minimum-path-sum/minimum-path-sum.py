class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[-1 for i in range(m)]for j in range(n)]
        def f(i,j):
            if i>=n or j>=m:
                return float('inf')
            if i==n-1 and j==m-1:
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            down=f(i+1,j)
            right=f(i,j+1)
            dp[i][j]=grid[i][j]+min(down,right)
            return dp[i][j]
        return f(0,0)