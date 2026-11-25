# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(root,subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            
            if root.val==subroot.val:
                return check(root.right,subroot.right) and check(root.left,subroot.left)
            else:
                return False
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        if root.val==subRoot.val:
            a= check(root,subRoot)
            if a:
                return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)