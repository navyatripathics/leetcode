# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a=[]
        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            heapq.heappush(a,node.val)
            inorder(node.right)
        inorder(root)
        for i in range(k):
            b=heapq.heappop(a)
        return b