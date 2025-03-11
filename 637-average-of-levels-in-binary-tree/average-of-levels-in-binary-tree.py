# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque([root])
        b=[]
        while q:
            size=len(q)
            a=0
            for i in range(size):
                node=q.popleft()
                a+=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            b.append(a/size)
        return b