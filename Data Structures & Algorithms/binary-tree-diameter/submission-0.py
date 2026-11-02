# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        temp=0
        def rec(root):
            nonlocal temp
            if not root:
                return 0
            a=rec(root.left)
            b=rec(root.right)

            temp=max(temp,a+b)
            return 1 + max(a,b)
        
        rec(root)
        return temp