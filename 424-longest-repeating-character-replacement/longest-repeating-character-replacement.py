class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        left=0
        hash={}
        maxf=0
        maxlen=0
        for right in range(left,n):
            if s[right] in hash:
                hash[s[right]]+=1
            else:
                hash[s[right]]=1
            maxf=max(maxf,hash[s[right]])
            if (right-left+1-maxf)<=k:
                maxlen=max(maxlen,right-left+1)
            else:
                hash[s[left]]-=1
                left+=1
                maxf-=1
        return maxlen