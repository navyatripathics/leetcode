class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)]for j in range(m)]
        def f(row,col):
            if row==m-1 and col==n-1:
                return 1
            if row >= m or col >= n:
                return 0

            if dp[row][col]!=-1:
                return dp[row][col]
            down=f(row+1,col)
            right=f(row,col+1)
            dp[row][col]=down+right
            return dp[row][col]
        return f(0,0)
            