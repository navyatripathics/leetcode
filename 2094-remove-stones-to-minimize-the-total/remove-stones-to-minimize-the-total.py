class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap=[]
        maxheap = [-p for p in piles]
        heapq.heapify(maxheap)
        while k:
            a=-heapq.heappop(maxheap)
            b=ceil(a/2)
            heapq.heappush(maxheap,-b)
            k=k-1
        return -sum(maxheap)