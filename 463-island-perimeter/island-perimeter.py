from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        q=deque()
        visited=set()
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    q.append((r,c))
                    visited.add((r,c))
        parameter=0
        while q:
            r,c=q.popleft()
            for dr,dc in d:
                nr,nc= r+dr,c+dc
                if nr<0 or nr>=row or nc<0 or nc>=col or grid[nr][nc]==0:
                    parameter+=1
                elif (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
        return parameter
