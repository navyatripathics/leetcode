# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binarySearch(l,r):
            while r>=l:
                mid=(l+r)//2
                if isBadVersion(mid):
                    r=mid-1
                else:
                    l=mid+1
            return l
        return binarySearch(1,n)