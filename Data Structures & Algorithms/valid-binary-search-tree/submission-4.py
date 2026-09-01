# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right):
            if not root:
                return True

            if not (left < root.val < right):
                return False
        
            # on each iteration for the left node, all numbers have to be less than the root node,
            # and every root node preceding that, so we create an upper limit for the left subtree

            # on the right, it is the same but opposite, we need a lower limit to ensure every value
            # is greater than our root
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        return valid(root, float("-inf"), float("inf"))



