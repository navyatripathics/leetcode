class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        m=[]
        for a in s:
            if a not in d:
                d[a]=1
            else:
                d[a]+=1
        sorted_chars = sorted(d.items(), key=lambda x: x[1], reverse=True)
        for key,value in sorted_chars:
            m.append(key*value)
        return ''.join(m)