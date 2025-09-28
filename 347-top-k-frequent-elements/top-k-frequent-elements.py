class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        res=[]
        heap=[]
        for key,value in d.items():
            heapq.heappush(heap,(-value,key))
        for i in range(k):
            freq,val=heapq.heappop(heap)
            res.append(val)
        return res