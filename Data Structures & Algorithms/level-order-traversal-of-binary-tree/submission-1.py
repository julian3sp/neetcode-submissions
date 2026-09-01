# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            cur_level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    cur_level.append(node.val)

                    q.append(node.left)
                    q.append(node.right)
            if cur_level:
                res.append(cur_level)

        return res

            
                
