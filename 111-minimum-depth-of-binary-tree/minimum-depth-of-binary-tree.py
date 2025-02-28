# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans=float('inf')
        if not root:
            return 0
        q=deque()
        q.append((root,1))    #node,count
        while q:
            size=len(q)
            for i in range(size):
                node,count=q.popleft()
                if node.left:
                    q.append((node.left,count+1))
                if node.right:
                    q.append((node.right,count+1))
                if node.left==None and node.right==None:
                    ans=min(ans,count)
        return ans
