# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        def isSame(root,subRoot):
            if root == None and subRoot == None:
                return True
            
            if root == None or subRoot == None:
                return False
            
            if root.val != subRoot.val:
                return False
            
            left = isSame(root.left,subRoot.left)
            right = isSame(root.right,subRoot.right)

            return left and right
        

        if isSame(root,subRoot):
            return True
        else:
            l = self.isSubtree(root.left,subRoot)
            r = self.isSubtree(root.right,subRoot)
            
        if l or r:
            return True
        else:
            return False

        
