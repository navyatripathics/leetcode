import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq=[]
        for row in matrix:
            for i in row:
                heapq.heappush(pq,-i)
                if len(pq)>k:
                    heapq.heappop(pq)
        return -pq[0]