# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if max(q.val, p.val) < cur.val:
                cur = cur.left
            elif min(q.val, p.val) > cur.val:
                cur = cur.right
            else:
                return cur

        


