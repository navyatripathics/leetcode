class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        start, max_len = 0, 1

        for i in range(n):
            dp[i][i] = True  # single char is palindrome

        for end in range(1, n):
            for start_idx in range(end):
                if s[start_idx] == s[end]:
                    if end - start_idx == 1 or dp[start_idx+1][end-1]:
                        dp[start_idx][end] = True
                        if end - start_idx + 1 > max_len:
                            max_len = end - start_idx + 1
                            start = start_idx
        return s[start:start+max_len]
