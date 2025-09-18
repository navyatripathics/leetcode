class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d={}
        z=[]
        o=[]
        res=[]
        for i,j in matches:
            if i not in d:
                d[i]=0
            if j not in d:
                d[j]=0
            d[j]+=1
        for key,value in d.items():
            if value==0:
                z.append(key)
            if value==1:
                o.append(key)
        z.sort()
        o.sort()
        res.append(z)
        res.append(o)
        return res