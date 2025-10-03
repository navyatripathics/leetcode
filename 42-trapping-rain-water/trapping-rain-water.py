class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        left=0
        right=len(height)-1
        lmax,rmax=0,0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=lmax:
                    lmax=height[left]
                else:
                    total+=lmax-height[left]
                left+=1
            else:
                if height[right]>=rmax:
                    rmax=height[right]
                else:
                    total+=rmax-height[right]
                right-=1
        return total
