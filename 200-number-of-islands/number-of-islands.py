from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count=0
        n=len(grid)
        m=len(grid[0])
        
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        visited=set()
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            visited.add((r,c))
             #mark the value of grid at the row r and col c visited
            while q:
                row,col=q.popleft()
                for dr,dc in direction:
                    new_r,new_c=row+dr,col+dc
                    if 0<=new_r<n and 0<=new_c<m and grid[new_r][new_c]=='1':
                        grid[new_r][new_c]="0"
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
        return count
