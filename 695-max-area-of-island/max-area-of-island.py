from collections import deque
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_area = 0
        
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            area = 1
            while queue:
                row,col=queue.popleft()
                for dr,dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < rows and 0 <= new_c < cols and grid   [new_r][new_c] == 1 and (new_r, new_c) not in visited):
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        area += 1
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))

        return max_area
            