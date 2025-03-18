from collections import deque
from typing import Optional

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        flag = False 

        while q:
            node = q.popleft()

            if not node:
                flag = True
            else:
                if flag:  
                    return False 
                
                q.append(node.left)
                q.append(node.right)

        return True
