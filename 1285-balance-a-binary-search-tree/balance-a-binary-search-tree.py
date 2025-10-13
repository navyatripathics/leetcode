# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
        inorder(root)
        def balance(l,r):
            if l>r:
                return None
            mid=(l+r)//2
            newNode=TreeNode(a[mid])
            newNode.left=balance(l,mid-1)
            newNode.right=balance(mid+1,r)
            return newNode
        return balance(0,len(a)-1)