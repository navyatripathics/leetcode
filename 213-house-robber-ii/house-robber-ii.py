class Solution:
    def f(self,nums):
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[-1]*(n)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            rob=nums[i]+dp[i-2]
            notrob=dp[i-1]
            dp[i]=max(rob,notrob)
        return dp[n-1]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if not nums:
            return 0
        if n==1:
            return nums[0]
        nums1=nums[0:n-1]
        nums2=nums[1:n]
        
        return max(self.f(nums1),self.f(nums2))