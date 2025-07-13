# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result=0
        def dfs(node,summ):
            nonlocal result
            if not node:
                return
            summ=summ*10+node.val
            if not node.left and not node.right:
                result+=summ
            else:
                dfs(node.left,summ)
                dfs(node.right,summ)
        dfs(root,0)
        return result