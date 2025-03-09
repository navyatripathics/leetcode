from collections import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = [False] * n 

        for i in range(n):
            if not visited[i]:
                count += 1
                q = deque([i])
                visited[i] = True

                while q:
                    node = q.popleft()

                    for j in range(n):
                        if isConnected[node][j] == 1 and not visited[j]:
                            visited[j] = True
                            q.append(j)
        return count
