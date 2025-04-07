class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[-1 for i in range(m)]for j in range(n)]
        def f(i,j):
            if i>=n or j>=m:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            if i==n-1 and j==m-1:
                return 1
            
            if dp[i][j]!=-1:
                return dp[i][j]
            down=f(i+1,j)
            right=f(i,j+1)
            dp[i][j]=down+right
            return dp[i][j]
        return f(0,0)