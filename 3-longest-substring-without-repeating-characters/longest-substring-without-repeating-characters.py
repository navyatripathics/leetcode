class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash={}
        left=0
        ans=0
        if not s:
            return 0
        if len(s)==1:
            return 1
        for right in range(len(s)):
            if s[right] not in hash:
                hash[s[right]]=1
            else:
                while s[right] in hash:
                    hash[s[left]]-=1
                    if hash[s[left]]==0:
                        del hash[s[left]]
                    left+=1
                hash[s[right]]=1
            ans=max(right-left+1,ans)
        return ans