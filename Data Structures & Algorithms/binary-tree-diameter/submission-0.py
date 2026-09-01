# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # initialize diameter
        diameter = 0

        def dfs(root):
            nonlocal diameter
            #base condition for depth
            if not root:
                return 0
            #dfs
            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, (left + right))

            return 1 + max(left, right)
        #execute dfs
        dfs(root)
        return diameter


