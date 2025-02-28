from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute=0
        q=deque()
        visited=set()
        n,m=len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    visited.add((i,j))
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            row,col,minute=q.popleft()
            for dr,dc in direction:
                new_row,new_col=dr+row,dc+col
                if 0<=new_row<n and 0<=new_col<m and grid[new_row][new_col]==1 and (new_row,new_col) not in visited:
                    grid[new_row][new_col]=2
                    q.append((new_row,new_col,minute+1))
                    visited.add((new_row,new_col))
        return -1 if any(1 in row for row in grid) else minute