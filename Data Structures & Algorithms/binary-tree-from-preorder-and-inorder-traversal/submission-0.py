# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        freq = {val: i for i, val in enumerate(inorder)}

        self.preindex = 0

        def calTree(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder[self.preindex]
            self.preindex += 1

            root = TreeNode(root_val)

            idx = freq[root_val]

            root.left = calTree(in_left, idx - 1)
            root.right = calTree(idx + 1, in_right)

            return root

        return calTree(0, len(inorder) - 1)

           

        
