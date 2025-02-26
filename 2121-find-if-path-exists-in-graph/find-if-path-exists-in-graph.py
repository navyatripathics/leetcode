
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        visited.add(source)
        stack=[source]
        while stack:
            node=stack.pop()
            if node==destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in visited:
                    visited.add(nei_node)
                    stack.append(nei_node)
                    if nei_node==destination:
                        return True
        return False
        