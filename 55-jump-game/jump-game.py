class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def func(nums):
            maxind=0
            for i in range(len(nums)):
                if i>maxind:
                    return False
                maxind=max(maxind,i+nums[i])
            return True
        return func(nums)        