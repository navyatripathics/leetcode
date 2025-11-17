class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        count=0
        visited=[False]*n
        def dfs(i):
            for j in range(n):
                if isConnected[i][j]==1 and not visited[j]:
                    visited[j]=True
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
        return count