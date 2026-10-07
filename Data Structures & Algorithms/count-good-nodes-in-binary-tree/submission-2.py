# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(root, maxVal):
            if not root:
                return 0
            maxVal = max(maxVal, root.val)
            left = dfs(root.left, maxVal)
            right = dfs(root.right, maxVal)

            if root.val >= maxVal:
                return 1 + left + right
            else:
                return left + right
        self.res = dfs(root, root.val)
        return self.res