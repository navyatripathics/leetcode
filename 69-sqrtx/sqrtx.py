class Solution:
    def mySqrt(self, x: int) -> int:
        def binarySearch(l,r):
            if l>r:
                return r
            mid=(l+r)//2
            if mid*mid==x:
                return mid
            elif mid*mid>x:
                return binarySearch(l,mid-1)
            else:
                return binarySearch(mid+1,r)
        return binarySearch(0,x)

