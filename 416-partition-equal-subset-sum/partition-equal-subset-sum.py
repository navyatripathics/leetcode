class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        summ=sum(nums)
        if summ%2!=0:
            return False
        target=summ//2
        dp=[[-1 for _ in range(target+1)]for _ in range(n)]
        def f(ind,target):
            if target==0:
                return True
            if ind==0:
                return nums[0]==target
            if dp[ind][target]!=-1:
                return dp[ind][target]
            nottake=f(ind-1,target)
            take=False
            if nums[ind]<=target:
                take=f(ind-1,target-nums[ind])
            dp[ind][target]=take or nottake
            return dp[ind][target]
        return f(n-1,target)