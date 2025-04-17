from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        left = []
        right = [0] * n
        lmax = height[0]
        for i in range(n):
            lmax = max(lmax, height[i])
            left.append(lmax)

        rmax = height[n-1]
        for i in range(n-1, -1, -1):
            rmax = max(rmax, height[i])
            right[i] = rmax

        summ = 0
        for i in range(n):
            summ += min(left[i], right[i]) - height[i]

        return summ
