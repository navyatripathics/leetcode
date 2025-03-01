"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q=deque([root])
        ans=[]
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                ans.append(node)
                if i < size - 1:
                    node.next = q[0]
                if i == size - 1:  # End of level
                    ans.append("#")
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
                