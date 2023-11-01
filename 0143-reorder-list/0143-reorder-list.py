# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        ptr1 = head
        ptr2 = prev

        while ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next
            ptr1.next = ptr2
            ptr2.next = temp1
            ptr1 = temp1 
            ptr2 = temp2
        

        return head

