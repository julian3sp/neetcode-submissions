"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        deep_copy = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            deep_copy[cur] = copy
            cur = cur.next
        cur = head

        while cur:
            copy = deep_copy[cur]
            copy.next = deep_copy[cur.next]
            copy.random = deep_copy[cur.random]
            cur = cur.next
        return deep_copy[head]
