from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            rob = nums[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0)
            not_rob = dp[i - 1]
            dp[i] = max(rob, not_rob)

        return dp[n]
