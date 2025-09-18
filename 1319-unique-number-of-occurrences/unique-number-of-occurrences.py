class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        v=[]
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return len(set(d.values()))==len(d)