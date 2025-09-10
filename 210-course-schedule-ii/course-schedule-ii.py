from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        visited = set()        # fully processed
        visiting = set()       # currently in recursion stack
        order = []             # topological order (reverse)

        def dfs(node):
            if node in visiting:   # cycle detected
                return False
            if node in visited:
                return True

            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            order.append(node)   # postorder appending
            return True

        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return []   # cycle found → no valid order
        return order[::-1]       # reverse to get correct order
