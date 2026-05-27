# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def calHeight(root):
            if root is None:
                return True

            leftHeight = calHeight(root.left)    
            rightHeight = calHeight(root.right)   

            if not leftHeight:
                self.balanced = False
            
            if not rightHeight:
                self.balanced = False
            
            if abs(leftHeight-rightHeight) > 1:
                self.balanced = False
            return 1+max(leftHeight,rightHeight)

        calHeight(root)
        return self.balanced

