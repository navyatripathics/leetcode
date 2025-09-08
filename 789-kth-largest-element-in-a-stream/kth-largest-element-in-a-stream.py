class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap=[num for num in nums]
        self.k=k
        heapq.heapify(self.minheap)
        while len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
    def add(self, val: int) -> int:
        
        if len(self.minheap)<self.k:
            heapq.heappush(self.minheap,val)
        elif val>self.minheap[0]:
            heapq.heapreplace(self.minheap,val)
        return self.minheap[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)