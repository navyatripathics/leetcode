import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        heap=[-count for count in freq.values()]
        heapq.heapify(heap)
        interval=0
        while heap:
            temp=[]
            work=0
            for _ in range(n+1):
                if heap:
                    cnt=heapq.heappop(heap)
                    work+=1
                    if cnt+1<0:
                        temp.append(cnt+1)
            for cnt in temp:
                heapq.heappush(heap,cnt)
            if heap:
                interval+=n+1
            else:
                interval+=work
        return interval