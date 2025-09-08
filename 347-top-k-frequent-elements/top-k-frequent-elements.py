class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        maxheap=[]
        a=[]
        for key,value in d.items():
            heapq.heappush(maxheap,(-value,key))
        for i in range(k):
            freq,num=heapq.heappop(maxheap)
            a.append(num)
        return a