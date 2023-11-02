# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverseLinkedList(head):
            prev = None
            curr = head

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return prev
        
        newHead = reverseLinkedList(head)
        
        dummy = ListNode(0)
        dummy.next = newHead
        prev = dummy
        curr = dummy.next
        i = 1
        
        while i < n:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
            
        curr.next = None

        return (reverseLinkedList(dummy.next))

            

        