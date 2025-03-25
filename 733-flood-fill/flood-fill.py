from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        original_color = image[sr][sc]
        
        if original_color == color:  # Avoid infinite loop
            return image
        q=deque([(sr,sc)])
        image[sr][sc]=color
        direction=[(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            row,col=q.popleft()
            for dr,dc in direction:
                new_r,new_c=dr+row,dc+col
                if 0<=new_r<m and 0<=new_c<n and image[new_r][new_c]==original_color:
                    image[new_r][new_c] = color
                    q.append((new_r,new_c))
        return image