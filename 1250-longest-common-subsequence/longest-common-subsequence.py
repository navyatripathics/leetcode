class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for _ in range(m)]for _ in range(n)]
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]=1+solve(i-1,j-1)
            else:
                dp[i][j]=max(solve(i-1,j),solve(i,j-1))
            return dp[i][j]
        return solve(n-1,m-1)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for i in range(n):
            dp[i][0]=0
        for j in range(m):
            dp[0][j]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]