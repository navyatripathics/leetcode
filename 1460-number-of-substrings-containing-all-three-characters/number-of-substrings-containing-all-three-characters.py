class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        hash=defaultdict(int)
        count=0
        for right in range(len(s)):
            hash[s[right]]+=1
            while hash['a']>0 and hash['b']>0 and hash['c']>0:
                count +=len(s)-right
                hash[s[left]]-=1
                left+=1
        return count
