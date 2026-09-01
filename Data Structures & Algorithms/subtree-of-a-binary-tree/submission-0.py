# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def matchTrees(root, subRoot):

            if not root and not subRoot:
                return True

            if root and subRoot and root.val == subRoot.val:
                return matchTrees(root.left, subRoot.left) and matchTrees(root.right, subRoot.right)
            else:
                return False


        if not root or not subRoot: 
            return False
        
        
        if matchTrees(root, subRoot):
            return True

        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        


