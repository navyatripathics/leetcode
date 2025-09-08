class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        sorted_d=sorted(d.items(),key=lambda item:item[1],reverse=True)
        l=[]
        for i in range(k):
            l.append(sorted_d[i][0])
        return l