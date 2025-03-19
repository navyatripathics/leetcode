class Solution:
    def f(self,index,nums,dp):
        if (index==0):
            return nums[0]
        if index<0:
            return 0
        if(dp[index]!=-1):
            return dp[index]
        rob=nums[index]+self.f(index-2,nums,dp)
        notrob=0+self.f(index-1,nums,dp)
        dp[index]=max(rob,notrob)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        return self.f(n-1,nums,dp)
        