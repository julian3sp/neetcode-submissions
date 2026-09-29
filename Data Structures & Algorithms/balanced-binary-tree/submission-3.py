# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def depth(root):
            if not root:
                return 0

            leftDepth = depth(root.left)
            if not self.isBalanced:
                return 0
            rightDepth = depth(root.right)

            if abs(leftDepth - rightDepth) > 1:
                self.isBalanced = False
                return 0
            
            return 1 + max(leftDepth, rightDepth)
        depth(root)

        return self.isBalanced