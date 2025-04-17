class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        map=[False]*n
        ds=[]
        res=[]
        def f(ds,map):
            
            if len(ds)==n:
                res.append(ds[:])
            for i in range(n):
                if nums[i] not in ds:
                    ds.append(nums[i])
                    map[i]=True
                    f(ds,map)
                    ds.pop()
                    map[i]=False
        f(ds,map)
        return res