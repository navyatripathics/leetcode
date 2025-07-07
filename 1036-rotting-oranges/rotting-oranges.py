from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        fresh=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        directions={(-1,0),(1,0),(0,-1),(0,1)}
        minute=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    newr,newc=r+dr,c+dc
                    if 0<=newr<row and 0<=newc<col and grid[newr][newc]==1:
                        grid[newr][newc]=2
                        q.append((newr,newc))
                        fresh-=1
            minute+=1
        return minute if fresh==0 else -1