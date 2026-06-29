class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        hash={}
        count=0
        maxf=0
        for right in range(len(s)):
            if s[right] in hash:
                hash[s[right]]+=1
            else:
                hash[s[right]]=1
            maxf = max(maxf, hash[s[right]])
            while (right-left+1)-maxf>k:
                hash[s[left]]-=1
                left+=1
            count=max(count,right-left+1)
        return count