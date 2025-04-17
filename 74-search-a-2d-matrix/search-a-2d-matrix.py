class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right=m*n-1
        while left<=right:
            mid=(left+right)//2
            mid_row,mid_col=mid//m,mid%m
            if matrix[mid_row][mid_col]==target:
                return True
            elif matrix[mid_row][mid_col]<target:
                left=mid+1
            else:
                right=mid-1
        return False