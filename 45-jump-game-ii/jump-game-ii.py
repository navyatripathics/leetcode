class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def f(ind):
            if ind>=n-1:
                return 0
            mini=float('inf')
            if dp[ind]!=-1:
                return dp[ind]
            for i in range(1,nums[ind]+1):
                if ind+i<n:
                    mini=min(mini,1+f(ind+i))
            dp[ind]=mini
            return dp[ind]
        return f(0)