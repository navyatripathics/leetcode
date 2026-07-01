import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in nums:
            heapq.heappush(heap,-i)
        for j in range(k):
            b=-heapq.heappop(heap)
        return b
        