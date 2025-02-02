class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=set(range(0,n+1))
        num=set(nums)
        a=s.difference(num)
        return a.pop()