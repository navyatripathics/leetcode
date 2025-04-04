from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1 for _ in range(len(triangle[i]))] for i in range(n)]

        def f(i, j):
            if i == n - 1:
                return triangle[i][j]
            if dp[i][j] != -1:
                return dp[i][j]
            down = f(i + 1, j)
            diag = f(i + 1, j + 1)
            dp[i][j] = min(down, diag) + triangle[i][j]
            return dp[i][j]

        return f(0, 0)
