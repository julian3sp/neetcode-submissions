# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        minVal = float('-inf')
        maxVal = float('inf')

        def dfs(root, minVal, maxVal):
            if not root:
                return True

            left = dfs(root.left, minVal, root.val)
            right = dfs(root.right, root.val, maxVal)

            return (minVal < root.val and root.val < maxVal and left and right)

        return dfs(root, minVal, maxVal)

