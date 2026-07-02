class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        heap=[]
        res=[]
        for key,v in d.items():
            heapq.heappush(heap,(-v,key))
        for _ in range(k):
            value,key=heapq.heappop(heap)
            res.append(key)
        return res