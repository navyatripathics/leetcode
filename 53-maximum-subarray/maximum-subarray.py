#Kadane's Algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum=nums[0]   
        summ=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],curr_sum+nums[i])
            summ=max(summ,curr_sum)
        return summ 