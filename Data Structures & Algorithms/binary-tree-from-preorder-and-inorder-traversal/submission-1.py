# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # the first value in preorder will always be the root
        # the same first value in the inorder traversal divides 
        # the left and right subtrees

        indices = {val : ind for ind, val in enumerate(inorder)}

        self.pre_indx = 0

        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_indx]
            self.pre_indx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        return dfs(0, len(inorder) - 1)







        


        
        