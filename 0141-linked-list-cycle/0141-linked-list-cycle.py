# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nextToPrev = {}

        cur = head

        while cur:
            if cur.next in nextToPrev:
                return True
            nextToPrev[cur.next] = cur
            cur = cur.next
        
        return False

        