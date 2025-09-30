class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        left=0
        maxi=0
        for right in range(len(s)):
            if s[right] in d and d[s[right]]>=left:
                left=d[s[right]]+1
            d[s[right]]=right
            maxi=max(maxi,right-left+1)
        return maxi