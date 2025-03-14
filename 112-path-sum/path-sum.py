# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) ->bool:
        if not root:
            return False
        q=deque([(root,root.val)])
        while q:
            node,curr_sum=q.popleft()
            if not node.left and not node.right and curr_sum==targetSum:
                return True
            if node.left:
                q.append((node.left,curr_sum+node.left.val))
            if node.right:
                q.append((node.right,curr_sum+node.right.val))
        return False