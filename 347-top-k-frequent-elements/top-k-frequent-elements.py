class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        a=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        sorted_d=sorted(d.items(),key=lambda item:item[1],reverse=True)
        for i in range(k):
            a.append(sorted_d[i][0])      
        return a  