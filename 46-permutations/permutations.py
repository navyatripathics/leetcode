class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        def f(ind,nums):
            if ind==n:
                res.append(nums[:])
            for i in range(ind,n):
                nums[ind],nums[i]=nums[i],nums[ind] #swap
                f(ind+1,nums)
                nums[ind],nums[i]=nums[i],nums[ind] #undo the swap
        f(0,nums)
        return res