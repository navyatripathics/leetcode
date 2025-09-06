
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        maxheap=[]
        for a in s:
            if a not in d:
                d[a]=1
            else:
                d[a]+=1
        for key,value in d.items():
            heapq.heappush(maxheap,(-value,key))
        m=[]
        while maxheap:
            freq,char=heapq.heappop(maxheap)
            m.append(char*-freq)
        return "".join(m)