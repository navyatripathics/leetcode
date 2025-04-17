class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}  # {char: index}
        n = len(s)
        if n == 0:
            return 0
        left = 0
        right = 0
        maxcount = 0

        while right < n:
            if s[right] not in hashmap or hashmap[s[right]] < left:
                hashmap[s[right]] = right
                maxcount = max(maxcount, right - left + 1)
                right += 1
            else:
                left = hashmap[s[right]] + 1
        return maxcount
