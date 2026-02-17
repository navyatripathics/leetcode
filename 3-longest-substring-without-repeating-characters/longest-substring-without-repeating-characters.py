class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash={}
        max_len=0
        left=0
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
            max_len=max(max_len,right-left+1)
        return max_len
