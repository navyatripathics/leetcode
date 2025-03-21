class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        dest=n-1
        res=[]
        def dfs(src,path,dest):
            path.append(src)
            if src==dest:
                res.append(path[:])
            else:
                for i in graph[src]:
                    dfs(i,path,dest)
            path.pop()
        dfs(0,[],dest)
        return res
        
