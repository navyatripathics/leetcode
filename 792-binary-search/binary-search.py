class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l,r):
            while(r>=l):
                mid=(l+r)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    return binarySearch(l,mid-1)
                else:
                    return binarySearch(mid+1,r)
            return -1
        return binarySearch(0,len(nums)-1)