from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        q = deque([root])

        while q:
            node = q.popleft()

            # Check if left child exists
            if node.left:
                # If it's a leaf node, add its value
                if not node.left.left and not node.left.right:
                    res += node.left.val
                # Otherwise, add it to the queue for further processing
                q.append(node.left)

            # Always add the right child if it exists
            if node.right:
                q.append(node.right)

        return res
