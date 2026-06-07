# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        self.maximum = float('-inf')
        def findMax(root):
            if root == None:
                return 0
            
            left = findMax(root.left)
            right = findMax(root.right)

            if left < 0:
                left = 0
            
            if right < 0:
                right = 0


            addition = root.val + left + right
            self.maximum = max(self.maximum,addition)

            return root.val + max(left,right)
        
        result = findMax(root)
        return max(self.maximum,result)
