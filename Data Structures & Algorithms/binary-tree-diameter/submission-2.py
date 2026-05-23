# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0 
        def calcuateHeight(root):
            if not root:
                return 0
            leftheight = calcuateHeight(root.left)
            rightheight = calcuateHeight(root.right)

            self.diameter = max(leftheight + rightheight,self.diameter)

            height = 1+max(leftheight,rightheight)
            return height

        calcuateHeight(root)
        return self.diameter
        