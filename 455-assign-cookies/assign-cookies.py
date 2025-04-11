class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n=len(g)
        m=len(s)
        g.sort()
        s.sort()
        l=0
        r=0
        while(l<m and r<n):
            if s[l]>=g[r]:
                l+=1
                r+=1
            else:
                l+=1
        return r