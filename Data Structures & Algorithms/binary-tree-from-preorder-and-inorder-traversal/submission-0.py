# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        pre_index = 0
        # the first value in preorder will always be the root
        # the same first value in the inorder traversal divides 
        # the left and right subtrees
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i
        
        def dfs(left, right):
            nonlocal pre_index
            if left > right:
                return None
            root = TreeNode()
            root.val = preorder[pre_index]
            pre_index += 1
            mid = hashmap[root.val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root
        return dfs(0, len(inorder) - 1)


        
        