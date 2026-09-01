# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        dummy = head

        while dummy and dummy.next:
            dummy = dummy.next.next
            node = node.next
            if dummy == node:
                return True

            
        return False