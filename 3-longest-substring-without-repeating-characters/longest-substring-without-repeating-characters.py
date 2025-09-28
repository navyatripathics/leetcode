class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        left=0
        maxi=0
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left+=1
            d.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi