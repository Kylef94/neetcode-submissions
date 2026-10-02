# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        cur1 = head.next
        cur2 = head
        while cur1 and cur1.next:
            if cur1 == cur2: return True
            cur1 = cur1.next.next
            cur2 = cur2.next

        return False
        