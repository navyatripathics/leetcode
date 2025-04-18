import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        a=[]
        heap=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for key,values in d.items():
            heapq.heappush(heap,(-values,key))
        for i in range(k):
            a.append(heapq.heappop(heap)[1])
        return a
        