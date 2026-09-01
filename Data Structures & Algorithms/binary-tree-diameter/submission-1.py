# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(root):
            nonlocal diameter
            #base case
            if not root:
                return 0
            
            #recursive call
            left_height = height(root.left)
            right_height = height(root.right)

            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)
        height(root)
        return diameter


