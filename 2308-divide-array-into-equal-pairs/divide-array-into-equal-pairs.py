class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        size=len(nums)
        a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for j in a.values():
            if j%2!=0:
                return False
        return True 