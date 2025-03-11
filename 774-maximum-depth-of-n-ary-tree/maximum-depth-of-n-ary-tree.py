"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth=0
        q=deque([root])
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node.children:
                    q.extend(node.children)

            depth+=1
        return depth
