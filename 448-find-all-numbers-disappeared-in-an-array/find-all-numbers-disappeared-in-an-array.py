class Solution(object):
    def findDisappearedNumbers(self, nums):
        n=len(nums)
        s=set(range(1,n+1))
        n=set(nums)
        a=s.difference(n)
        return list(a)