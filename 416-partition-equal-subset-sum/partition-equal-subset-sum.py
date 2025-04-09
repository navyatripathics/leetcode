#TABULATION
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        summ=sum(nums)
        target=summ//2
        if summ%2!=0:
            return False
        dp=[[False for i in range(target+1)]for j in range(n)]
        for i in range(n):
            dp[i][0]=True
        if nums[0]<target:
            dp[0][nums[0]]=True
        for ind in range(1,n):
            for t in range(1,target+1):
                not_take=dp[ind-1][t]
                take=False
                if nums[ind]<=t:
                    take=dp[ind-1][t-nums[ind]]
                dp[ind][t]=take or not_take
        return dp[n-1][target]